""" This module works as a mediator in a two bot players game of connect 4.
It must be called like in the following example:

    python3 Connect4.py juan.py pepa.py

where juan.py and pepa.py are the playing bots.

Bots must implement the following function:

    def column(grid:list, disc:str) -> int:

where "grid" is a representation for the game board (grid from now on).
This is the empty grid:

[['_', '_', '_', '_', '_', '_', '_', '_', '_'],
 ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
 ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
 ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
 ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
 ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
 [ 5,   5,   5,   5,   5,   5,   5,   5,   5]]

And "disc" is the piece (coloured disc) the bot plays with. The piece can be "@" or "#".

The returnin value is the column number (0 to 8) where a bot desires to drop a disc.

Here you have a non empty grid:

[['_', '@', '_', '_', '_', '_', '_', '_', '_'],
 ['_', '@', '_', '_', '_', '_', '_', '_', '_'],
 ['_', '#', '_', '_', '_', '_', '_', '_', '_'],
 ['_', '@', '_', '_', '_', '_', '_', '_', '_'],
 ['_', '@', '_', '_', '#', '_', '_', '_', '_'],
 ['_', '#', '_', '_', '#', '_', '@', '_', '_'],
 [ 5,   -1,  5,   3,   3,   5,   4,   5,   5]]

An empty position on the grid is represented by "_" character.

The last row of the grid keeps for every column the row where a disc could be dropped.

On the previous grid example the state can be summarised as follows:

    5 is the column coordinate for a drop on columns 0, 2, 3, 5, 7 and 8
    3 is the column coordinate for a drop on column 4
    no further drops can be done on column 1 (it is full of discs)
    
A bot can change the grid as needed because the received grid is a copy of the current game grid.

A bot can lose a game by returning a column out of the range 0 to 8 or a column full of discs.

The command line can be redirected to a file for a further study of "what happened"

    python3 Connect4.py juan.py pepa.py > gameSummary.txt

Here you have a more comprensive chart of the coordinates system:

grid[row][colum]
    |_|_|_|_|_|_|_|_|_|0
    |_|_|_|_|_|_|@|_|_|1
    |_|_|_|_|_|_|#|@|_|2
    |_|_|_|_|_|#|@|#|_|3
    |_|_|_|_|@|@|#|@|#|4
    |@|#|#|@|@|@|#|#|#|5
    |4|4|4|4|3|2|0|1|3|6
     0 1 2 3 4 5 6 7 8

    -- grid[6][4] is 3
    -- next place that could be filled in column 7 is grid[6][7], this is 1

Here you have a quite simple (and silly) rules compliant bot:

    from random import randrange
    def myName():
        return "JUAN"
    def column(grid:list, disc:str) -> int:
        return randrange(0, 9, 1)

@@@@@@@@@@@@@@@@@@@@     "MAY THE FORCE BE WITH YOU"     ####################
"""

import importlib, sys, os.path, copy

def getCleanGrid():
    return [['_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
            [5, 5, 5, 5, 5, 5, 5, 5, 5]]

def printGrid(grid):
	tc = range(9)
	tr = range(6)
	for r in tr:
		for c in tc:
			sys.stdout.write("|"+grid[r][c])
		sys.stdout.write("|"+str(r))
		print()
	print (" 0 1 2 3 4 5 6 7 8 ")

def legalDrop(grid,column):
	return column in range(9) and grid[6][column] >= 0

def dropDisc(grid, column, disc):
	grid[grid[6][column]][column] = disc
	grid[6][column] = grid[6][column] - 1

def checkState(grid, column, disc) -> int:
    #Vertical
    row = grid[6][column]
    #let's count down
    if row <= 2:
        n = 1
        for row in range(row+1,row+3+1,+1):
            if grid[row][column] == disc:
                n = n + 1
            else:
                break
            if n >= 4:
                return 1

    #Horizontal and diagonals
    n = n45 = n315 = 1
    f_min_out = -1
    f_max_out = 6
    row = row45 = row135 = row315 = row225 = grid[6][column]
    #let's count towards right
    c_max_out = column+3+1
    c_max_out = c_max_out if c_max_out <= 9 else 9
    check_n = check_n45 = check_n315 = True
    for col in range(column+1,c_max_out,+1):
	#0 degrees
        if check_n and grid[row][col] == disc:
            n = n + 1
        else:
            check_n = False
	#45 degrees
        row45 = row45 - 1
        if row45 > f_min_out:
            if check_n45 and grid[row45][col] == disc:
                n45 = n45 + 1
            else:
                check_n45 = False
	#315 degrees
        row315 = row315 + 1
        if row315 < f_max_out:
            if check_n315 and grid[row315][col] == disc:
                n315 = n315 + 1
            else:
                check_n315 = False
    if n >= 4 or n45 >=4 or n315 >= 4:
        return 1
    #let's count towards left
    c_min_out = column-3-1
    c_min_out = c_min_out if c_min_out >= -1 else -1
    check_n = check_n45 =check_n315 = True
    for col in range(column-1,c_min_out,-1):
	#180 degrees
        if check_n and grid[row][col] == disc:
            n = n + 1
        else:
            check_n = False
	#225 degrees
        row225 = row225 + 1
        if check_n45 and row225 < f_max_out:
            if grid[row225][col] == disc:
                n45 = n45 + 1
            else:
                check_n45 = False
	#135 degrees
        row135 = row135 - 1
        if row135 > f_min_out:
            if check_n315 and grid[row135][col] == disc:
                n315 = n315 + 1
            else:
                check_n315 = False
    if n >= 4 or n45 >=4 or n315 >= 4:
        return 1
    # let's check tie condition
    freeCells = 0
    for col in range(0,9):
        freeCells += grid[6][col] + 1
        if freeCells > 1:
            return 0
    return 2

## MAIN
if __name__ == "__main__":
    if sys.argv.__len__() < 3:
        print("Missing arguments. Usage: Connect-4 <botA.py> <botB.py>")
        quit()

    if not os.path.exists(sys.argv[1]):
        print("Module ", sys.argv[1], " not found. Check name and path!")
        quit()
    else:
        players=[sys.argv[1][:-3]]
    if not os.path.exists(sys.argv[2]):
        print("Module ", sys.argv[2], " not found. Check name and path!")
        quit()
    else:
        players.append(sys.argv[2][:-3])

    boot0=importlib.import_module(players[0])
    boot1=importlib.import_module(players[1])

    discs = ["@","#"]
    print("Player 1 is", players[0], "playing with", discs[0])
    print("Player 2 is", players[1], "playing with", discs[1])
    summary=[]
    for rnd in range(2):
    # Init game
        playerTurn = rnd
        playerDisc = discs[playerTurn]
        print(players[playerTurn], "starts confrontation", rnd+1) 
        gameFinished = False
        grid = getCleanGrid()
        printGrid(grid)
        movNumber=1
        while not gameFinished:
            # Get player's movement
            gridCopy = copy.deepcopy(grid)
            if playerTurn == 0:
                column=boot0.column(gridCopy,playerDisc)
            else:
                column=boot1.column(gridCopy,playerDisc)
            # Check movement's legality (if ilegal movement, proclaim winner and move on next round)
            if not legalDrop(grid,column):
                gameFinished = True
                summary.append(players[playerTurn] + " loses confrontation " + str(rnd+1) + \
                               " due to an illegal disc drop attempt on column " + str(column) + \
                               " on movement " + str(movNumber))
                print(summary[-1])
            else:
                print(players[playerTurn], "drops disc", discs[playerTurn], "on column", column)
                # Check what would happen if a playerDisc were dropped on column
                gameState=checkState(grid,column,playerDisc)
                if gameState == 1 :
                    # there will be a winner.
                    # Report winner
                    summary.append(players[playerTurn] + " wins confrontation " + str(rnd+1) + \
                                   " on movement " + str(movNumber))
                    print(summary[-1])
                elif gameState == 2:
                    # There will be a tie.
                    # Report tie
                    summary.append("Confrontation " + str(rnd+1) + \
                                   " ended in tie on movement " + str(movNumber))
                    print(summary[-1])
                gameFinished = gameState >= 1
                # Make movement 
                dropDisc(grid,column,playerDisc)
                printGrid(grid)
                print()
                movNumber += 1
                if not gameFinished :
                    # Game still will go on. Change turn
                    playerTurn+=1
                    playerTurn%=2
                    playerDisc=discs[playerTurn]
    print()
    print("-------------SUMMARY-------------")
    for eachMsg in summary:
        print("--",eachMsg)
    

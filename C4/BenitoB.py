from random import choice, randrange


def column(grid: list, disc: str) -> int:
    lines = grid[6]
    for i in range(len(lines)):  # check if I am about to win in any line
        if lines[i] == -1:
            continue
        if checklines(grid, lines[i], i, disc):
            return i
    # input()
    for i in range(len(lines)):  # check if enemy is about to win in any line
        if lines[i] == -1:
            continue
        if checklines(grid, lines[i], i, opponentdisc(disc)):
            return i
    # if none of the above return a valid number then just return a random
    return getrandomline(lines)


def checklines(grid: list, x: int, y: int, disc: str) -> bool:
    """
    Checks the specified positions on the grid to see if the param disc can win in each of them.
    :param grid: the current state of the grid
    :param x: vertical coordinate to check
    :param y: horizontal coordinate to check
    :param disc: disc to look for into the grid
    :return: the line in where the disc is about to win
    """
    linewins = False
    steps, chance, linechecked = 0, 0, 0
    # first check: horizontal
    for j in range(-3, 4):
        if y + j > 8 or y + j < 0:
            # print("Continue horizontal -> y+j:", y + j)
            continue
        if grid[x][y + j] == disc:  # if it finds another disc, add 1 to the win chance
            chance += 1
            if chance > 2:
                return True
        elif grid[x][y + j] == opponentdisc(disc):  # if it finds an opponent's disc
            # reset the counter
            chance = 0
        if chance > 2:
            linewins = True

    # second check: vertical
    chance = 0  # reset the variable to reuse it again
    for i in range(-3, 4):
        if x + i > 5 or x + i < 0:
            # print("Continue vertical -> ", x + i)
            continue
        if grid[x+i][y] == disc:
            chance += 1
            if chance > 2:
                return True
        elif grid[x+i][y] == opponentdisc(disc):
            chance = 0
        if chance > 2:
            linewins = True

    # third check: /
    chance = 0
    j = -3
    for i in range(3, -4, -1):
        if x + i > 5 or x + i < 0 or y + j > 8 or y + j < 0:
            # print("Continue / -> x:", x + i, " y:", y + j)
            j += 1  # also add it here so that it is always increased, even if it skips a round
            continue
        if grid[x+i][y+j] == disc:
            chance += 1
            if chance > 2:
                return True
        elif grid[x+i][y+j] == opponentdisc(disc):
            chance = 0
        if chance > 2:
            linewins = True
        j += 1

    # fourth check: \
    chance = 0
    for i in range(-3, 4):
        if x + i > 5 or x + i < 0 or y + i > 8 or y + i < 0:
            # print("Continue \\ -> x", x + i, "y:", y + i)
            continue
        if grid[x + i][y + i] == disc:
            chance += 1
            if chance > 2:
                return True
        elif grid[x + i][y + i] == opponentdisc(disc):
            chance = 0
        if chance > 2:
            linewins = True

    return linewins


def getrandomline(lines: list) -> int:
    """
    Gets a random line from the list of posibilities, making sure it is a valid one
    :param lines: list of posibilites to choose from
    :return: the choosen line making sure it has room for the disc
    """
    i = randrange(0, 9, 1)
    ret = lines[i]
    while ret == -1:
        i = randrange(0, 9, 1)
        ret = lines[i]
        print("Escogido:", ret)
    return i


def opponentdisc(disc: str) -> str:
    """
    Help function to get the oponent's disc.
    :param disc: Current disc being analized
    :return: Oponent's disc
    """
    if disc == '@':
        oponent = '#'
    else:
        oponent = '@'
    return oponent

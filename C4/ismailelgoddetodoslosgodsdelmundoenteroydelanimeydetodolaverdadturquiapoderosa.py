from random import randint
from math import floor

from Connect4 import *

CONST_MAX_COLUMNS   = 9
CONST_MAX_ROWS      = 6

def WillDiscFall(grid, line, square):
    if (grid[CONST_MAX_ROWS][square] != line):
        return True
    else:
        return False

def MeetsLimits(grid, line, square) -> bool:
    if (line >= CONST_MAX_ROWS \
        or line < 0):
        return False

    if (square >= CONST_MAX_COLUMNS \
        or square < 0):
        return False

    if (grid[CONST_MAX_ROWS][square] < 0):
        return False

    return True

def CheckWinEx(grid, disc, line, square) -> int:
    # Straight up
    if (line - 3 >= 0):
        if (grid[line - 1][square] == disc):
            if (grid[line - 2][square] == disc):
                if (grid[line - 3][square] == '_'):
                    if (MeetsLimits(grid, line, square)):
                        return square

    # Lateral right
    if (MeetsLimits(grid, line, square + 3)):
        if (grid[line][square + 1] == disc):
            if (grid[line][square + 2] == disc):
                if (grid[line][square + 3] == '_' and not WillDiscFall(grid, line, square + 3)):
                    if (MeetsLimits(grid, line, square + 3)):
                        return square + 3
            elif (grid[line][square + 2] == '_' and not WillDiscFall(grid, line, square + 2)):
                if (grid[line][square + 3] == disc):
                    if (MeetsLimits(grid, line, square + 2)):
                        return square + 2
        elif (grid[line][square + 1] == '_' and not WillDiscFall(grid, line, square + 1)):
            if (grid[line][square + 2] == disc):
                if (grid[line][square + 3] == disc):
                    if (MeetsLimits(grid, line, square + 1)):
                        return square + 1

    # Lateral left
    if (MeetsLimits(grid, line, square - 3)):
        if (grid[line][square - 1] == disc):
            if (grid[line][square - 2] == disc):
                if (grid[line][square - 3] == '_' and not WillDiscFall(grid, line, square - 3)):
                    if (MeetsLimits(grid, line, square - 3)):
                        return square - 3
            elif (grid[line][square - 2] == '_' and not WillDiscFall(grid, line, square - 2)):
                if (grid[line][square - 3] == disc):
                    if (MeetsLimits(grid, line, square - 2)):
                        return square - 2
        elif (grid[line][square - 1] == '_'):
            if (grid[line][square - 2] == disc):
                if (grid[line][square - 3] == disc):
                    if (MeetsLimits(grid, line, square - 1)):
                        return square - 1

    # Diagonal right
    if (MeetsLimits(grid, line - 3, square + 3)):
        if (grid[line - 1][square + 1] == disc):
            if (grid[line - 2][square + 2] == disc):
                if (grid[line - 3][square + 3] == '_' and not WillDiscFall(grid, line - 3, square + 3)):
                    if (MeetsLimits(grid, line - 3, square +3)):
                        return square + 3
            elif (grid[line - 2][square + 2] == '_' and not WillDiscFall(grid, line - 2, square + 2)):
                if (grid[line - 3][square + 3] == disc):
                    if (MeetsLimits(grid, line - 2, square + 2)):
                        return square + 2
        elif (grid[line - 1][square + 1] == '_' and not WillDiscFall(grid, line - 1, square + 1)):
            if (grid[line - 2][square + 2] == disc):
                if (grid[line - 3][square + 3] == disc):
                    if (MeetsLimits(grid, line - 1, square + 1)):
                        return square + 1

    # Diagonal left
    if (MeetsLimits(grid, line - 3, square - 3)):
        if (grid[line - 1][square - 1] == disc):
            if (grid[line - 2][square - 2] == disc):
                if (grid[line - 3][square - 3] == '_' and not WillDiscFall(grid, line - 3, square - 3)):
                    if (MeetsLimits(grid, line - 3, square -3)):
                        return square - 3
            elif (grid[line - 2][square - 2] == '_' and not WillDiscFall(grid, line - 2, square - 2)):
                if (grid[line - 3][square - 3] == disc):
                    if (MeetsLimits(grid, line - 2, square - 2)):
                        return square - 2
        elif (grid[line - 1][square - 1] == '_' and not WillDiscFall(grid, line - 1, square - 1)):
            if (grid[line - 2][square - 2] == disc):
                if (grid[line - 3][square - 3] == disc):
                    if (MeetsLimits(grid, line - 1, square - 1)):
                        return square - 1

    
    return -1

def CheckWin(grid: list, disc: str) -> int:
    for line in range(CONST_MAX_ROWS - 1, 0, -1):
        for square in range(0, CONST_MAX_COLUMNS):
            if (grid[line][square] == disc):
                pos = CheckWinEx(grid, disc, line, square)
                if (pos != -1):
                    return pos

    return -1

firstTurn = True
def CheckBestMove(grid: list, disc: str, otherDisc = str) -> int:
    #
    # It is first turn and we are the first player, play middle always
    #
    global firstTurn
    if (firstTurn and disc == "@"):
        firstTurn = False
        return floor(CONST_MAX_COLUMNS / 2)

    val = None
    for line in range(CONST_MAX_ROWS - 1, 0, -1):
        for square in range(0, CONST_MAX_COLUMNS):
            if (not WillDiscFall(grid, line, square)):
                val = IsImportantMove(grid, line, square, disc, otherDisc)
                if (val != -1):
                    return val

    # First loop through squares to check if next turn win
    for square in range(0, CONST_MAX_COLUMNS - 1):
        if (not MeetsLimits(grid, 0, square)):
            continue

        if (WillGiveVictory(grid, square, disc, disc)):
            return square

    return GetOptimalMove(grid, disc, otherDisc)


def WillGiveVictory(grid, square, disc, otherDisc) -> bool:
    # Edit the grid to add the square then check if opponent can win next turn
    grid[grid[CONST_MAX_ROWS][square]][square] = otherDisc

    if (CheckWin(grid, disc) == -1):
        return False

    return True


def GetOptimalMove(grid, disc, otherDisc) -> int:
    # Can't find anything, do random
    num = randint(0, CONST_MAX_COLUMNS - 1)
    while (not MeetsLimits(grid, 0, num) or WillGiveVictory(grid, num, otherDisc, disc)):
        num = randint(0, CONST_MAX_COLUMNS - 1)

    return num

#
# All moves here apply for opponent and us, the same move that opponent may do we might do as well
#
def IsImportantMove(grid, line, square, disc, otherDisc) -> int:
    #
    # Problem:
    #   Opponent has two discs together and may be able to put a third one next to them while two spaces are open
    #   If we allow this move opponent has two win options and we can only block one
    #
    # Example:
    #   |_|_|#|#|_|@|       -       |_|#|#|_|_|
    # 
    # Solution:
    #   We must choose any of the 3 spots to block now, leaving only 1 position for opponent
    #   |_|@|#|#|_|@|       -       |_|#|#|@|_|
    #
    for curDisc in (disc, otherDisc):
        if (MeetsLimits(grid, line, square + 4)):
            if (grid[line][square] == '_' and not WillDiscFall(grid, line, square)):
                if (grid[line][square + 1] == '_' and not WillDiscFall(grid, line, square + 1)):
                    if (grid[line][square + 2] == curDisc):
                        if (grid[line][square + 3] == curDisc):
                            if (grid[line][square + 4] == '_' and not WillDiscFall(grid, line, square + 4)):
                                return square + 1
                elif (grid[line][square + 1] == curDisc):
                    if (grid[line][square + 2] == curDisc):
                        if (grid[line][square + 3] == '_' and not WillDiscFall(grid, line, square + 3)):
                            if (grid[line][square + 4] == '_' and not WillDiscFall(grid , line, square + 4)):
                                return square + 3


    #
    # Problem:
    #   Opponent has two discs separated by empty space each of which has an empty space on the other side
    #   If we allow this move opponent has two win options and we can only block one
    #
    # Example:
    #   |_|#|_|#|_|
    #
    # Solution:
    #   Block the middle empty space when the structure is found
    #
    for curdisc in (disc, otherDisc):
        if (MeetsLimits(grid, line, square - 1) and MeetsLimits(grid, line, square + 3)):
            if (grid[line][square - 1] == '_' and not WillDiscFall(grid, line, square - 1)):
                if (grid[line][square + 1] == '_' and not WillDiscFall(grid, line, square + 1)):
                    if (grid[line][square + 2] == curDisc):
                        if grid[line][square + 3] == '_' and not WillDiscFall(grid, line, square + 3):
                            return square + 1


    #
    # Problem:
    #   Opponent has 3 vertical discs and 3 lateral discs in a T-pose, leaving top space open and left or right space open
    #   If we allow this move opponent has two win options and we can only block one
    #
    # Example:
    #   |_|_|_|_|_|     -     |_|_|_|_|_|
    #   |_|#|#|#|_|     -     |_|#|#|#|_|
    #   |@|@|#|@|_|     -     |_|#|#|@|#|
    #   |@|@|#|@|_|     -     |_|@|#|#|@|
    #
    # Solution:
    #   We must block the top connecting piece before it happens, effectively blocking all sides
    #   |_|_|_|_|_|     -     |_|_|_|_|_|
    #   |_|#|@|#|_|     -     |_|#|@|#|_|
    #   |@|@|#|@|_|     -     |_|#|#|@|#|
    #   |@|@|#|@|_|     -     |_|@|#|#|@|
    #
    for curDisc in (disc, otherDisc):
        if (MeetsLimits(grid, line - 2, square) and MeetsLimits(grid, line - 2, square - 1) and MeetsLimits(grid, line - 2, square + 1)):
            if (grid[line][square] == curDisc):
                if (grid[line - 1][square] == curDisc):
                    if (grid[line - 2][square] == '_'):
                        if (grid[line - 2][square - 1] == curDisc):
                            if (grid[line - 2][square + 1] == curDisc):
                                return square


    #
    # Problem:
    #   Opponent has 2 diagonals led by and tailed by his disc, one of which is 3 pieces and the other may be 2
    #   If we block this move incorrectly, opponent may be able to take advantage of our move to win with the other diagonal
    #
    # Example:     (Opponent turn)
    #   |_|_|_|_|#|      ->      |_|_|_|_|#|
    #   |#|_|_|#|@|      ->      |#|_|_|#|@|
    #   |@|_|_|@|@|      ->      |@|#|_|@|@|
    #   |#|#|_|@|#|      ->      |#|#|_|@|#|
    #   |@|@|@|#|@|      ->      |@|@|@|#|@|
    #
    # Solution: 
    #   We must block the optimal position 
    #                 (My turn)
    #   |_|_|_|_|#|      ->      |_|_|_|_|#|
    #   |#|_|_|#|@|      ->      |#|_|_|#|@|
    #   |@|_|_|@|@|      ->      |@|#|_|@|@|
    #   |#|#|_|@|#|      ->      |#|#|_|@|#|
    #   |@|@|@|#|@|      ->      |@|@|@|#|@|
    #
    for curDisc in (disc, otherDisc):
        if (MeetsLimits(grid, line - 4, square + 1) and MeetsLimits(grid, line - 4, square - 3)):
            if (grid[line - 1][square - 2] == curDisc):
                if (grid[line - 1][square - 1] == '_' and not WillDiscFall(grid, line - 1, square - 1)):
                    if (grid[line - 2][square - 2] == '_' and not WillDiscFall(grid, line - 2, square - 2)):
                        if (grid[line - 3][square] == curDisc):
                            if (grid[line - 3][square - 3] == curDisc):
                                if (grid[line - 4][square + 1] == curDisc):
                                    return square - 2

    # Mirror
    for curDisc in (disc, otherDisc):
        if (MeetsLimits(grid, line - 4, square + 3) and MeetsLimits(grid, line - 4, square - 1)):
            if(grid[line - 1][square + 2] == curDisc):
                if (grid[line - 1][square + 1] == '_' and not WillDiscFall(grid, line - 1, square + 1)):
                    if (grid[line - 2][square + 2] == '_' and not WillDiscFall(grid, line - 2, square + 2)):
                        if (grid[line - 3][square] == curDisc):
                            if (grid[line - 3][square + 3] == curDisc):
                                if (grid[line - 4][square - 1] == curDisc):
                                    return square + 2


    #
    # Problem:
    #   Opponent has 2 vertical discs with open top which connects to a lateral missing 1 disc
    #   If we allow this move opponent has two win options and we can only block one
    #
    # Example:
    #   |_|#|_|#|       -       |#|#|_|_|
    #   |#|@|@|@|       -       |@|#|@|#|
    #   |#|@|#|@|       -       |#|@|@|#|
    #
    # Solution:
    #   We must block the top connecting piece before it happens, effectively blocking all sides 
    #   |@|#|_|#|       -       |#|#|_|@|
    #   |#|@|@|@|       -       |@|#|@|#|
    #   |#|@|#|@|       -       |#|@|@|#|
    #
    for curDisc in (disc, otherDisc):
        if (MeetsLimits(grid, line - 2, square + 3)):
            if (grid[line - 1][square] == curDisc):
                if (grid[line - 2][square + 1] == curDisc):
                    if (grid[line - 2][square + 2] == curDisc):
                        if (grid[line - 2][square + 3] == '_' and not WillDiscFall(grid, line - 2, square + 3)):
                            return square + 3
                    elif (grid[line - 2][square + 2] == '_' and not WillDiscFall(grid, line - 2, square + 2)):
                        if (grid[line - 2][square + 3] == curDisc):
                            return square + 2
                elif (grid[line - 2][square + 1] == '_' and not WillDiscFall(grid, line - 2, square + 1)):
                    if (grid[line - 2][square + 2] == curDisc):
                        if (grid[line - 2][square + 3] == curDisc):
                            return square + 1


    #
    # Problem:
    #   Opponent has a diagonal connecting to a horizontal
    #   If we allow this move opponent has two win options and we can only block one
    #
    # Example:
    #   |_|_|_|_|
    #   |#|_|#|#|
    #   |@|_|@|#|
    #   |#|@|@|@|
    #
    # Solution:
    #   We must block the diagonal piece, since blocking the connecting piece will give a free win move to the opponent
    #   |_|_|_|@|
    #   |#|_|#|#|
    #   |@|_|@|#|
    #   |#|@|@|@|
    #
    for curDisc in (disc, otherDisc):
        if (MeetsLimits(grid, line - 3, square + 3)):
            if (grid[line - 2][square] == curDisc):
                if (grid[line - 1][square + 1] == '_' and not WillDiscFall(grid, line - 1, square + 1)):
                    if (grid[line - 2][square + 1] == '_' and not WillDiscFall(grid, line - 2, square + 1)):
                        if (grid[line - 2][square + 2] == curDisc):
                            if (grid[line - 2][square + 3] == curDisc):
                                if (grid[line - 3][square + 3] == '_' and not WillDiscFall(grid, line - 3, square + 3)):
                                    return square + 3


    return -1


def myName():
    return "ismailelgoddetodoslosgodsdelmundoenteroydelanimeydetodolaverdadturquiapoderosa"

def column(grid:list, disc:str) -> int:
    # Can I win with 1 movement?
    col = CheckWin(grid, disc)
    if (col != -1):
        print("Found win condition at", col, "for disk", disc)
        return col

    otherDisc = "@" if disc == "#" else "#"

    # Can opponent win with 1 movement?
    col = CheckWin(grid, otherDisc)
    if (col != -1):
        print("Found win condition at", col, "for disk", otherDisc)
        return col

    # Whats the best move for winning next turn
    return CheckBestMove(grid, disc, otherDisc)
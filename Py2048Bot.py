import Py2048
from Py2048 import Py2048
import sys
import copy

# generic optimization function
# value_function must take Py2048 object as input and return some valuation
# on the nonnegative real numbers, the larger number the better.

#algo just takes each turn by trying each of left, right, up, down on a copy and doing whichever has the best outcome per this function on one try (remember, there is randomness involved).

def one_pass_value_max(value_function):
    moves = [Py2048.up, Py2048.down, Py2048.left, Py2048.right]
    board = Py2048()
    board.render()
    openSpace = True
    while openSpace or not board.gameOver():
        bestMove = None
        bestValue = 0
        for move in moves:
            copyboard = copy.deepcopy(board)
            move(copyboard)
            val = value_function(copyboard)
            if val >= bestValue:
                bestMove = move
                bestValue = val
        openSpace = bestMove(board)
        board.render()
# a fairly simple metric for how "good" a board is.
# returns a nonnegative real number
def density(board):
    s = 0
    c = 0
    for i in range(board.length):
        for j in range(board.length):
            if board.table[i][j] != 0:
                s += board.table[i][j]
                c += 1
    return s/c # note that c will always be nonzero because a board is never all 0
# does the classic beginner strategy: go down and right alternately
def trivial():
    board = Py2048()
    board.render()
    openSpace = True
    counter = 0
    while openSpace or not board.gameOver():
        if counter % 2:
            openSpace = board.right()
        else:
            openSpace = board.down()
        board.render()
        counter += 1

if __name__ == '__main__':
    modes = {'standard': lambda: one_pass_value_max(density), 'trivial':trivial}
    if len(sys.argv) < 2:
        print("Usage: python Py2048Bot.py [mode]")
    else:
        modes.get(sys.argv[1], trivial)()

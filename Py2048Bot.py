import Py2048
from Py2048 import Py2048
import sys
import copy

moves = [Py2048.up, Py2048.down, Py2048.left, Py2048.right]


# function that runs an optimization function.
# optfunc must take a single board parameter and return el in moves
# for optimization functions that use more paramters, wrap them in a lambda
def run_opt(optfunc):
    board = Py2048()
    openSpace = True
    while openSpace or not board.gameOver():
        bestMove = optfunc(board)
        openSpace = bestMove(board)
        board.render()
        print("\n\n")
        
# returns a tuple: (move, value)
# the move is only used by outermost loop

# exact same as one_pass_value_max but bases its values on recursive calls. In other words, it explores possibilities to depth k
# uses average performance of each treebranch
def k_away(board, value_function, k):
    if k == 0:
        return (moves[0], value_function(board)) # moves[0] is arbitrary - we will never use this
    bestMove = None
    bestValue = 0
    sumValue = 0
    for move in moves:
        copyboard = copy.deepcopy(board)
        move(copyboard)
        val = k_away(copyboard, value_function, k-1)[1]
        sumValue += val
        if val >= bestValue:
            bestValue = val
            bestMove = move
    avgValue = sumValue / len(moves)
    return (bestMove, avgValue)

# generic optimization function
# value_function must take Py2048 object as input and return some valuation
# on the nonnegative real numbers, the larger number the better.

#algo just takes each turn by trying each of left, right, up, down on a copy and doing whichever has the best outcome per this function on one try (remember, there is randomness involved).

def one_pass_value_max(board, value_function):
    bestMove = None
    bestValue = 0
    for move in moves:
        copyboard = copy.deepcopy(board)
        move(copyboard)
        val = value_function(copyboard)
        if val >= bestValue:
            bestMove = move
            bestValue = val
    return bestMove


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
# a potentially better metric ... weights larger values much more strongly
def valsquare(board):
    s = 0
    for i in range(board.length):
        for j in range(board.length):
            s += board.table[i][j] ** 2
    return s

def valueof(board, (x,y)):
    return (x - board.length//2)**2 + (y - board.length//2) ** 2

def valsquare_plus(board): # valsquare, but weights squares near the corners and edge more than inside
    s = 0
    for i in range(board.length):
        for j in range(board.length):
            s += board.table[i][j] ** 2 * valueof(board,(i,j))
    return s
def valsquare_dist(board): # product of all pairs of elements in grid divided by (distance^2 + 1)
    s = 0
    for i in range(board.length):
        for j in range(board.length):
            for ip in range(board.length):
                for jp in range(board.length):
                    s += (board.table[i][j])*(board.table[ip][jp])/(1 + (i-ip)**2 + (j-jp)**2 )
    return s
# a potentially even better metric: values when large numbers are next to one another
def valadj(board):
    s = 0
    # add left/right adjacents
    for i in range(board.length-1):
        for j in range(board.length):
            s += (board.table[i][j]*board.table[i+1][j])**2
    for i in range(board.length):
        for j in range(board.length-1):
            s += (board.table[i][j]*board.table[i][j+1])**2


def valmax(board):
    return board.get_max_val()
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
    modes = {'standard': lambda: run_opt(lambda b: k_away(b, valsquare, 4)[0]), 'trivial':trivial}
    if len(sys.argv) < 2:
        print("Usage: python Py2048Bot.py [mode]")
    else:
        modes.get(sys.argv[1], trivial)()

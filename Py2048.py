import numpy as np
import random
import copy


class Py2048:
    # Initializes board to all 0's (empty).
    # Performs put operation once
    def __init__(self):
        self.table = np.zeros( (4,4) ) # 0 = empty square.
        self.nzeros = 16 # how many squares are currently empty?
        self.max_val = 0
        self.put()

    # Places either a 2 or 4 on board in a position that is currently 0
    # Returns False if either there was no space to place a number, or
    # if there was exactly one place and the method call filled it.
    def put(self):
        if not self.nzeros: return False
        toPut = random.choice([2,4])
        if toPut > self.max_val:
            self.max_val = toPut
        all_places = [(i,j) for i in range(4) for j in range(4)]
        place = random.choice(filter(lambda p: self.table[p] == 0, all_places))
        self.table[place] = toPut
        self.nzeros -= 1
        # it's possible we just decremented nzeros to 0. in this case we should still return False
        # becasue the board is full
        return (self.nzeros != 0)

    # Shifts an elements in given row toward the end of row per 2048 rules
    # in typical rendering of 2048 board this represents a "right shift".
    # check is a bool. if check is True, the board will not be changed.
    # shift returns true iff some merge occurs
    def shift(self, check):
        retval = False # return False unless some merge happens
        # row
        for r in range(4):
            # nonzero values from end of row to beginning
            from_end = []
            comb = False # was the last value in from_end already merged?
            for c in range(3,-1,-1):
                if self.table[r][c] != 0:
                    if comb or len(from_end) == 0 or self.table[r][c] != from_end[-1]:
                        from_end.append(self.table[r][c])
                    else: # comb is False and the values match
                        from_end[-1] *= 2 # double this value
                        retval = True # we have merged at least once, so we set the retval = True
                        comb = True # indicate that we combined
            if not check:
                for c in range(3,-1,-1):
                    if len(from_end) == 0:
                        self.table[r][c] = 0
                    else:
                        self.table[r][c] = from_end.pop(0) # from end starts at end so pop from 0
                        # we just assigned a new value to table. Check if it's larger than max_val
                        if self.table[r][c] > self.max_val:
                            self.max_val = self.table[r][c]
                            
        return retval
        
    # Copies table to shift all entries clockwise.
    # Helpful in using decomposed shift() method in up,down,left,right methods
    def cw(self):
        copytable = copy.deepcopy(self.table)
        for r in range(4):
            for c in range(4):
                self.table[r][c] = copytable[4-1-c][r]

    # Move operations.

    # Move operations return the value of self.put() after the move.
    # Thus they return False exactly when the board is full after the operation

    # A return of False on a move doesn't necessarily mean the game is over, but if the game is over, we
    # must have returned False on the last move.
                
    # Move operation that appears in +x direction to user
    def right(self):
        self.shift(False)
        return self.put()

    # Move operation that appears in -x direction to user
    def left(self):
        self.cw()
        self.cw()
        self.shift(False)
        self.cw()
        self.cw()
        return self.put()
    # Move operation that appears in +y direction to user
    def up(self):
        self.cw()
        self.shift(False)
        for i in range(3):
            self.cw()
        return self.put()

    # Move operation that appaers in -y direction to user
    def down(self):
        for i in range(3):
            self.cw()
        self.shift(False)
        self.cw()
        return self.put()
                

    # Returns true iff the entire board is full and none of up/down/left/right will let us merge anything.
    def gameOver(self):
        for i in range(4):
            self.cw() # rotate cw
            if self.shift(True):
                return False # means that we can advance the game by shifting this way
        # note that after 4 cws, the board is back in its original configuration.
        return True # nothing can save us :(

    def render(self):
        print(str(self.table))

    def get_max_val(self):
        return self.max_val
        
if __name__ == '__main__':
    board = Py2048()
    funcmap = {'up': board.up, 'down': board.down, 'left': board.left, 'right': board.right}
    openSpace = True # we set this via return values of move methods. We only check gameOver when openSpace is False.
    curr_max_val = 0
    while openSpace or not board.gameOver():
        if board.get_max_val() > curr_max_val:
            curr_max_val = board.get_max_val()
            print("Value " + str(board.get_max_val()) + " unlocked!")
        board.render()
        move_type = raw_input()
        if move_type == 'quit':
            break
        if move_type not in funcmap:
            print("Please enter a valid move.")
        else:
            funcmap[move_type]()
    print("Game Over!!!!")
        
        

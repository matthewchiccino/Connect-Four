#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from board_class import Board

# write your class below.
class Player:
    
    def __init__(self,checker):
        """ creates a object, checker and nummoves, nummoves is set to 0"""
        self.checker = checker
        self.num_moves = 0 
    def __repr__(self):
        """ return player and whatever checker they are """
        return 'Player' + ' ' + self.checker
    def opponent_checker(self):
        """ if self.checker is x than your opponent has to to O and vice versa"""
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
    def next_move(self, b):
        """ while true to continue looking until a valid number is inputed. 
        col will be the integer of the input given by user. if input of b.can_add_to(col)
        if true than 1 is added to num moves and print the result. else it tells the user to try agin"""
        while True: 
            col = int(input("Enter a column: "))
            if b.can_add_to(col) == True:
                self.num_moves += 1
                return col 
            else: 
                print('Try again!')
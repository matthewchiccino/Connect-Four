#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from board_class import Board
from player_class import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        
def process_move(p,b):
    """ prints whicher players turn it is, then gets next move by calling the nextmove method
    then adding it to the board using a board call. print a line then the boarrd.
    if its win for p.checker or the checker that is currenlty being played it will print p won in x amount of moves
    congras and return true, if the board is full it prints tie and returns true, else it returns false.    """
    print(str(p)  + "'s turn")
    nextmove = p.next_move(b)
    b.add_checker(p.checker, nextmove )
    print()
    print(b)
    if b.is_win_for(p.checker) :
        print(str(p) + ' wins in ' + str(p.num_moves) + ' moves.')
        print('Congratulations!')
        return  True
    elif b.is_full() :
        print('Its a tie!')
        return True 
    else:
        return False 
    
class RandomPlayer(Player):
    
    def next_move(self, b):
        """ inhertining from player class randomplayer makes random moves, the list of not full colums 
        is empty at first but using a for loop to go throught the indeces of board width. if that column 
        still can get added to then i will add the index. after going through the whole range, using random 
        it sleects anything in that list, moves += 1 and retunrs the column."""
        notfull= []
        for i in range(b.width):
            if b.can_add_to(i) == True :
                notfull += [i]
        rnum = random.choice(notfull)
        self.num_moves += 1
        return rnum
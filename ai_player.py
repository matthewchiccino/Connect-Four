#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from  game_logic import *

class AIPlayer(Player):
    """replacing the init inherited from player, i assert first given the instrcutions
    then i create self.checker tirbreak and lookahead."""
    def __init__(self, checker, tiebreak, lookahead):
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        self.checker = checker 
        self.tiebreak = tiebreak 
        self.lookahead = lookahead
        super().__init__(checker)
    
    def __repr__(self):
        """ replacing represent inherited from player, this gives the player their tiebreak strategy and lookahead."""
        return 'Player ' + self.checker + ' (' + self.tiebreak +', ' + str(self.lookahead) + ')'
    
    def max_score_column(self, scores):
        """ max scores list is initialy empty, then to get the biggest num i take the max.
        using a for loop to go through the all the scores. if scores[i] is equal to the biggest score
        that index is added to the list. based off their tirbreaking stragety i either return the left most 
        index right most index or use reandom choice."""
        maxscores = []
        bignum = max(scores)
        for i in range(len(scores)):
            if scores[i] == bignum :
                maxscores += [i] 
                
        if self.tiebreak == 'LEFT':
            return maxscores[0]
            
        elif self.tiebreak == 'RIGHT':
            return maxscores[-1]
        
        else:
            return random.choice(maxscores)
        
    def scores_for(self, b):
        """ i create a list with the same width of the board. using a for loop to go 
        through the whole list, using canaddto if that is false it means its full and the score
        for that row is -1, if its a win that its 100, its a win for the opponent than its a 0 
        and if the lookahead is 0 then its 50. else i add a checker to that column, intialize
        an opponent with similiar tiebreak strategy, opposite checker, and a lookahead of -1.
        opp socres is scores for opponent. if opp score is 100 than self losses and that column is a loss
        if opp score is 0 that means its a win for self. and if nothing happens its 50 for both.
        i remove checker after and return the scores."""
        scores = [1738] * b.width 
        for i in range(b.width):
            if b.can_add_to(i) == False:
                scores[i] = -1
            elif b.is_win_for(self.checker):
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[i] = 0
            elif self.lookahead == 0 :
                scores[i] = 50 
            else:
                b.add_checker(self.checker, i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)  
                if max(opp_scores) == 100:
                    scores[i] = 0  
                elif max(opp_scores) == 0:
                    scores[i] = 100 
                elif max(opp_scores) == 50:
                    scores[i] = 50  
                b.remove_checker(i)
        return scores
   
    def next_move(self, b):
        """ to get the next move i call on scores for to get the list, to get the best score 
        i call on maxscorecolumn and also inputting the scoreslist previouslly obtained.
        add 1 to moves and return best score."""
        scoreslist = self.scores_for(b)
        bestscore = self.max_score_column(scoreslist)
        self.num_moves += 1
        return bestscore
        
            
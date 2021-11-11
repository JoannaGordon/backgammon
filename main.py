# main.py

from board_class import *
from player_classes import *

import random as rand

def main():
    board = Board()
    
    player1 = Human(1)
    player2 = Human(-1)
    
    players = [player1, player2]
    players_turn = 0
    
    while not win():
        board.print_board()
        
        roll = dice_roll()
        
        players[players_turn].set_move()
        
        board.make_move(players[players_turn])
        
        players_turn = (players_turn + 1) % 2
        

def win():
    return False
    
def dice_roll():
    return [rand.randint(1, 6), rand.randint(1,6)]
    
if __name__ == "__main__":
    main()
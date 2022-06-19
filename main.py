# main.py

from board_class import *
from player_classes import *

import random as rand

icons = {
    3: '3',
    2: 'O',
    1: 'o',
    0: ' ',
    -1: 'x',
    -2: 'X',
    -3: '3'
}

def main():
    board = Board()
    
    player1 = Human(1)
    player2 = Human(-1)
    
    players = [player1, player2]
    players_turn = 0
    
    while not win():
        board.print_board()
        
        roll = dice_roll()
        print('It\'s player ' + icons[players[players_turn].number] + '\'s turn')
        print('The dice roll is: ' + str(roll[0]) + ' and ' + str(roll[1]))
        
        #moves = players[players_turn].get_valid_moves(board.board, roll)
        #print(moves)
        
        players[players_turn].set_move(board.board, roll)
        
        board.make_move(players[players_turn].checkers_moves, players[players_turn].number)
        
        players_turn = (players_turn + 1) % 2
        

def win():
    return False
    
def dice_roll():
    return [rand.randint(1, 6), rand.randint(1,6)]
    
if __name__ == "__main__":
    main()
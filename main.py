# main.py

from board_class import *
from player_classes import *

import sys
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

def main(p1_mode = 'human', p2_mode = 'human', n_games = '1'):
    
    player1 = Human(1)
    player2 = Random(-1)
    
    players = [player1, player2]
    score = [0, 0]
    start_player = rand.randint(0, 1)
    
    for game_round in range(int(n_games)):
        players_turn = (start_player + game_round) % 2
        winner = run_game(players, players_turn)
        score[winner] = score[winner] + 1
        
    print('Overall ' + icons[players[0].number] + ' has ' + score[0] + ' wins and ' + icons[players[1].number] + ' has ' + score[1] + ' wins.')
    
def run_game(players, players_turn = 0):
    board = Board()
    
    while not board.check_win(players[players_turn].number*-1):
        board.print_board()
        
        roll = dice_roll()
        print('It\'s player ' + icons[players[players_turn].number] + '\'s turn')
        print('The dice roll is: ' + str(roll[0]) + ' and ' + str(roll[1]))
        
        players[players_turn].set_move(board.board, roll)
        
        board.make_move(players[players_turn].checkers_moves, players[players_turn].number)
        
        players_turn = (players_turn + 1) % 2
        
    print('Game over. Player ' + icons[players[players_turn].number*-1] + ' wins!')
    
    return (players_turn + 1) % 2
    
def dice_roll():
    return [rand.randint(1, 6), rand.randint(1,6)]
    
if __name__ == "__main__":
    main(sys.argv[1:])
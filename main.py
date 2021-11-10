from board_class import *
from player_classes import *

def main():
    board = Board()
    
    player1 = Human()
    player2 = Human()
    
    players = [player1, player2]
    players_turn = 0
    
    while not win():
        board.print_board()
        
        players[players_turn].set_move()
        
        board.make_move(players[players_turn].counter_moves)
        
        players_turn = (players_turn + 1) % 2
        

def win():
    return False
    
if __name__ == "__main__":
    main()
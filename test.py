# test.py

from board_class import *
from player_classes import *

def main():
    print('Running test file')
    test_board()
    
    #print()
    #test_no_valid_moves()
    #test_win()

def test_board():
    test_default_board()
    test_custom_board()
    test_board_updates_moves()
    
def test_default_board():
    print('Test that the default board it correct:   ', end='')
    test_board = Board()
    if test_board.board == [2, 0, 0, 0, 0, -5, 0, -3, 0, 0, 0, 5, -5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, -2, 0, 0]:
        print('Success')
    else:
        print('Fail')
        
def test_custom_board():
    print('Test that a custom board can be inputted:   ', end='')
    test_board = Board(board = [-2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, -5, 5, 0, 0, 0, -3, 0, -5, 0, 0, 0, 0, 2, 0, 0])
    if test_board.board == [-2, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, -5, 5, 0, 0, 0, -3, 0, -5, 0, 0, 0, 0, 2, 0, 0]:
        print('Success')
    else:
        print('Fail')
        
def test_board_updates_moves():
    print('Test the board updates to normal move moves:   ', end='')
    test_board = Board()
    test_board.make_move(['a3', 'a4'], 1)
    if test_board.board == [0, 0, 0, 1, 1, -5, 0, -3, 0, 0, 0, 5, -5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, -2, 0, 0]:
        print('Success')
    else:
        print('Fail')
        
        
        
        

def test_no_valid_moves():
    print('Test that when there are no valid moves the player\'s turn ends:   ', end='')
    test_board = Board(board = [-2, -2, -2, -2, -2, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0])
    test_player = Human(1)
    test_player.set_move(test_board.board, [1, 2])
    test_board.make_move(test_player.checkers_moves, test_player.number)
    if test_player.checkers_moves == [] and test_board.board == [-2, -2, -2, -2, -2, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]:
        print('Sucess')
    else:
        print('Fail')
        
def test_win():
    print('Test the board recognises a win:   ', end='')
    test_board = Board(board = [0, 0, 0, 0, 0, -5, 0, -3, 0, 0, 0, 0, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -2, 0, 0])
    if test_board.check_win(1) and not test_board.check_win(-1):
        print('Sucess')
    else:
        print('Fail')

if __name__ == "__main__":
    main()
# test.py

from board_class import *
from player_classes import *

def main():
    print('Running test file')
    test_board()

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
        

if __name__ == "__main__":
    main()
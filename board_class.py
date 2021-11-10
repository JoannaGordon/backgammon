# boardClass.py

class Board:
    def __init__(self):
        # Sets up board in starting position
        self.board = [2, 0, 0, 0 , 0, -5, 0, -3, 0, 0, 0, 5, -5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, -2]

    def print_board(self):
        # Prints the current state of the board to the console in text based fomat, seperating the two lines
        for i in range(12):
            print(self.board[i], end = ' ')
        print()
        for i in range(12):
            print(self.board[23-i], end = ' ')
        print()    
            
test_game = Board()
test_game.print_board()

print(test_game.board)
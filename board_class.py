# board_class.py

locations = {
    'a': 0, 
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
}

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
        
    def make_move(self, player):
        # Updates the board based on the player's move
        for move in player.counter_moves:
            # For all of the moves changes the numbe of counters in the location the move comes from and goes to
            self.board[locations[move[0]]] = self.board[locations[move[0]]] - player.number
            self.board[locations[move[0]]+player.number*int(move[1:])] = self.board[locations[move[0]]+player.number*int(move[1:])] + player.number
            
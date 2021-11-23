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

icons = {
    3: '3',
    2: 'O',
    1: 'o',
    0: ' ',
    -1: 'x',
    -2: 'X',
    -3: '3'
}

class Board:
    def __init__(self):
        # Sets up board in starting position
        
        self.board = [2, 0, 0, 0 , 0, -5, 0, -3, 0, 0, 0, 5, -5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, -2, 0, 0]

    def print_board(self):
        # Prints the current state of the board to the console in text based fomat, seperating the two lines
        
        print('abcdefghijkl')
        for i in range(5):
            for j in range (12):
                print(icons[int(round((abs(self.board[j])+2-i)/5))*int(self.board[j]/(abs(self.board[j])-0.01))], end='')
            print()
        print('\n ', end='')
        for i in range(5):
            print(icons[int(round((abs(self.board[24])-2+i)/5))*int(self.board[24]/(abs(self.board[24])-0.01))], end='')
        for i in range(5):
            print(icons[int(round((abs(self.board[25])-2+i)/5))*int(self.board[25]/(abs(self.board[25])-0.01))], end='')
        print('\n')
        for i in range(5):
            for j in range (12):
                print(icons[int(round((abs(self.board[23-j])-2+i)/5))*int(self.board[23-j]/(abs(self.board[23-j])-0.01))], end='')
            print()
        print('xwvutsrqponm')
        
    
    def make_move(self, player):
        # Updates the board based on the player's move
        
        for move in player.checkers_moves:
            # For all of the moves changes the numbe of counters in the location the move comes from and goes to
            self.board[locations[move[0]]] = self.board[locations[move[0]]] - player.number
            if self.board[locations[move[0]] + player.number*int(move[1:])]*player.number == -1:
                self.board[locations[move[0]] + player.number*int(move[1:])] = player.number
                self.board[int(24.5 + player.number/2)] = self.board[int(24.5 + player.number/2)] + 1
            else:
                self.board[locations[move[0]] + player.number*int(move[1:])] = self.board[locations[move[0]] + player.number*int(move[1:])] + player.number
                
            
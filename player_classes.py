# player_classes.py

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

class Player:
    def __init__(self, number):
        self.number = number
    
    
class Human(Player):
    def set_move(self, board, roll):
        move = input('Enter your move: ')
        while not self.valid_move(board, move, roll):
            move = input('Enter your move: ')
        
        self.checkers_moves = move.split()
        
    def valid_move(self, board, move, roll):
        if self.input_wrong(move):
            print('You have inputted your move in the wrong format please write the letter that coresponds to the location of the checker you want to move followed by the number of spaces you want to move it, repeating this for each of the checkers you want to move with a space between each. If you are removing checkers only include the letter location without a number')
            return False
        if self.too_many_moves(move, roll):
            print('You have input too many moves for the roll')
            return False
        if self.wrong_total_moves(move, roll):
            print('The total mnumber of spaces you are moving the checkers is incorrect for the dice roll')
            return False
        return True
        
        # check if len(checkers_moves) > 4
        # check if first element of string is a letter between a and x 
        # check if this is followed by a number or no number
        # check that number fits with the roll
        # check there is the correct number of moves for the roll (fit this in with the first point)
        # check the total moves is correct for the roll    
        
    def input_wrong(self, move):
        checkers_moves = move.split()
        for move in checkers_moves:
            try:
                locations[move[0]]
            except:
                return True
            if len(move) > 1:
                try:
                    int(move[1:])
                except:
                    return True        
        return False
        
    def too_many_moves(self, move, roll):
        if roll[0] == roll[1]:
            if len(move.split()) > 4:
                return True
        else:
            if len(move.split()) > 2:
                return True
        return False
        
    def wrong_total_moves(self, move, roll):
        # need to adjust this for the removing checkers phase
        checkers_moves = move.split()
        total = 0
        for move in checkers_moves:
            total = total + int(move[1:])
        if roll[0] == roll[1]:
            if total != roll[0]*4:
                return True
        else:
            if total != roll[0]+roll[1]:
                return True
        return False
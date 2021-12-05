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
        if self.no_checker(board, move):
            print('There are not checkers in the locations of all the moves you have input')
            return False
        if self.wrong_moves(move, roll):
            print('You cannot move your checkers that number of spaces')
            return False
        if self.wrong_total_moves(move, roll):
            print('The total mnumber of spaces you are moving the checkers is incorrect for the dice roll')
            return False
        if self.cant_land(board, move):
            print('Your checker can\'t land there')
            return False
        return True
        
        # check if correct number of moves
        # check if first element of string is a letter between a and x 
        # check if this is followed by a number or no number
        # check that number fits with the roll
        # check there is the correct number of moves for the roll (fit this in with the first point)
        # check the total moves is correct for the roll
        # check there are counters in the location inputted
        
        # check if there isn't an available move
        # check if the move uses more than one dice roll that the counter can do the inbetween step
        # declare which attempted move failed
        
        # should the input method be changed to input your moves indiviudally only not all together
        
        
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
        
    def no_checker(self, board, move):
        checkers_moves = move.split()
        for move in checkers_moves:
            if board[locations[move[0]]]*self.number < 1:
                return True
        return False
        
    '''  
    def too_many_moves(self, move, roll):
        if roll[0] == roll[1]:
            if len(move.split()) > 4:
                return True
        else:
            if len(move.split()) > 2:
                return True
        return False
    '''

    def wrong_moves(self, move, roll):
        # need to adjust this for the removing checkers phase
        checkers_moves = move.split()
        for move in checkers_moves:
            if int(move[1:]) != roll[0] and int(move[1:]) != roll[1] and int(move[1:]) != roll[0]+roll[1] and int(move[1:]) != roll[0]*2+roll[1] and int(move[1:]) != (roll[0]+roll[1])*2:
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
        
    def cant_land(self, board, move):
        checkers_moves = move.split()
        for move in checkers_moves:
            if board[locations[move[0]] + self.number*int(move[1:])]*self.number < -1:
                return True
            if locations[move[0]] + int(move[1:])*self.number < 0 or locations[move[0]] + int(move[1:])*self.number > 23:
                return True
        return False
            
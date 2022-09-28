# player_classes.py

from board_class import *

import random as rand

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

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x']

class Player:
    def __init__(self, number):
        self.number = number
        
    def get_valid_moves(self, board, roll):
    
        # converts the dice roll to a list of combinations of moves that could 
        #   be used 
        if roll[0] == roll[1]:
            roll_combinations = [[roll[0]]*4]
        else:
            roll_combinations = [roll, roll[::-1]]
        
        all_valid_moves = []            
        max_move_len = 0
        highest_dice_used = 0
        
        # loops through the combinations of moves generating valid moves in 
        #   each case and combining into a single list
        for roll_combination in roll_combinations:
            valid_moves = []
            movement = roll_combination[0]
            
            # generates a list of moves that could be done using the first
            #   move in the combination
            if board[int(24.5-0.5*self.number)] != 0: # need to place a checker case
                if board[int(11.5-11.5*self.number+(movement-1)*self.number)]*self.number >= -1:
                    valid_moves.append([letters[int(11.5-11.5*self.number+(movement-1)*self.number)], self.get_updated_board(board[:], letters[int(11.5-11.5*self.number+(movement-1)*self.number)])])
                    highest_dice_used = self.check_highest_dice_used(highest_dice_used, movement)
            elif all(space*self.number <= 0 for space in board[int(2.5-2.5*self.number):int(20.5-self.number*2.5)]): # need to remove a checker case
                if board[int((11.5+11.5*self.number)-(movement-1)*self.number)]*self.number > 0:
                    valid_moves.append([letters[int(11.5+11.5*self.number-(movement-1)*self.number)], self.get_updated_board(board[:], letters[int(11.5+11.5*self.number-(movement-1)*self.number)])])
                    highest_dice_used = self.check_highest_dice_used(highest_dice_used, movement)
            else: # normal move case
                for space in range(24):
                    if board[space]*self.number > 0:
                        if space+movement*self.number >= 0 and space+movement*self.number <= 23:
                            if board[space+movement*self.number]*self.number >= -1:
                                valid_moves.append([letters[space]+str(movement), self.get_updated_board(board[:], letters[space]+str(movement))])
                                highest_dice_used = self.check_highest_dice_used(highest_dice_used, movement)
            
            # repeates the process to add to the list moves using the later
            #   moves in the combination in conjunction with earlier moves
            for movement in roll_combination[1:]:
                for i in range(len(valid_moves)): # need to place a checker case
                    if valid_moves[i][1][int(24.5-0.5*self.number)] != 0:
                        if valid_moves[i][1][int(11.5-11.5*self.number+(movement-1)*self.number)]*self.number >= -1:
                            valid_moves.append([valid_moves[i][0] + ' ' + letters[int(11.5-11.5*self.number+(movement-1)*self.number)], self.get_updated_board(valid_moves[i][1][:], letters[int(11.5-11.5*self.number+(movement-1)*self.number)])])
                            highest_dice_used = self.check_highest_dice_used(highest_dice_used, movement)
                    elif all(space*self.number <= 0 for space in valid_moves[i][1][int(2.5-2.5*self.number):int(20.5-self.number*2.5)]): # need to remove a checker case
                        if valid_moves[i][1][(11.5+11.5*self.number)-(movement-1)*self.number]*self.number > 0:
                            valid_moves.append([valid_moves[i][0] + ' ' + letters[int(11.5-11.5*self.number+(movement-1)*self.number)], self.get_updated_board(valid_moves[i][1][:], letters[int(11.5-11.5*self.number+(movement-1)*self.number)])])
                            highest_dice_used = self.check_highest_dice_used(highest_dice_used, movement)
                    else: # normal move case
                        for space in range(24):
                            if valid_moves[i][1][space]*self.number > 0:
                                if space+movement*self.number >= 0 and space+movement*self.number <= 23:
                                    if valid_moves[i][1][space+movement*self.number]*self.number >= -1 :
                                        valid_moves.append([valid_moves[i][0] + ' ' + letters[space]+str(movement), self.get_updated_board(valid_moves[i][1][:], letters[space]+str(movement))])
                                        highest_dice_used = self.check_highest_dice_used(highest_dice_used, movement)

            # adds the valid moves from this iteration to the complete list and
            # determines the maximum number of moves it's possible to use
            for valid_move in valid_moves:
                all_valid_moves.append(valid_move[0])
                if len(valid_move[0]) > max_move_len:
                    max_move_len = len(valid_move[0])
         
        # creates a new list of moves that only uses the maximum number of moves
        #   or the highest number dice
        final_valid_moves = []
        for valid_move in all_valid_moves:
            if len(valid_move) == max_move_len:
                if str(highest_dice_used) in valid_move or letters[highest_dice_used-1] in valid_move or letters[24-highest_dice_used] in valid_move:
                    final_valid_moves.append(valid_move)
            
        return final_valid_moves
        
        
    def get_updated_board(self, board, move):
        if len(move) == 1:
            board[int(24.5 - self.number/2)] = board[int(24.5 - self.number/2)] - self.number
            if board[locations[move]]*self.number == -1:
                board[locations[move]] = self.number
                board[int(24.5 + self.number/2)] = board[int(24.5 + self.number/2)] - self.number
            else:
                board[locations[move]] = board[locations[move]] + self.number
        else:
            # For all of the moves changes the number of counters in the location the move comes from and goes to
            board[locations[move[0]]] = board[locations[move[0]]] - self.number
            if board[locations[move[0]] + self.number*int(move[1:])]*self.number == -1:
                board[locations[move[0]] + self.number*int(move[1:])] = self.number
                board[int(24.5 + self.number/2)] = board[int(24.5 + self.number/2)] - self.number
            else:
                board[locations[move[0]] + self.number*int(move[1:])] = board[locations[move[0]] + self.number*int(move[1:])] + self.number
 
        return board
        
    def check_highest_dice_used(self, highest_dice_used, movement):
        if movement > highest_dice_used:
            highest_dice_used = movement
        return highest_dice_used
        
    
class Human(Player):
    def set_move(self, board, roll):
        valid_moves = self.get_valid_moves(board, roll)
        
        if valid_moves == []:
            print('No available moves')
            self.checkers_moves = []
        else:
            move = input('Enter your move: ')
            #while not self.valid_move(board, move, roll):
            while move not in valid_moves:
                move = input('Enter your move: ')
            
            self.checkers_moves = move.split()
        
        # would be good to add back in a way to tell the user that there move 
        #   is in the wrong format or not a valid one
        
    '''
    
    def valid_move(self, board, move, roll):
        if self.input_wrong(move):
            print('You have inputted your move in the wrong format please write the letter that coresponds to the location of the checker you want to move followed by the number of spaces you want to move it, repeating this for each of the checkers you want to move with a space between each. If you are removing checkers only include the letter location without a number')
            return False
        if board[int(24.5-0.5*self.number)] != 0:
            return valid_checkers_in_bar()
        elif all(space*self.number <= 0 for space in board[int(2.5-2.5*self.number):int(20.5-self.number*2.5)]):
            return valid_remove_checkers()
        else:
            return valid_normal_move()
    
        
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
        
        # I think the structure needs to be changed, first work out if the move type is right then check the moves themselves
        
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
        
    def valid_checkers_in_bar():
        
        return True
        
    def valid_remove_checkers():
        return True
        
    def valid_normal_move():
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
        
    def no_checker(self, board, move):
        checkers_moves = move.split()
        for move in checkers_moves:
            if board[locations[move[0]]]*self.number < 1:
                return True
        return False
        
    ''' 
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
    '''        
    
 
class Random(Player):
    def set_move(self, board, roll):
        valid_moves = self.get_valid_moves(board, roll)
        
        if valid_moves == []:
            self.checkers_moves = []
        else:
            move = valid_moves[rand.randint(0, len(valid_moves)-1)]
            
            self.checkers_moves = move.split()
# player_classes.py

class Player:
    def __init__(self, number):
        self.number = number
    
    
class Human(Player):
    def set_move(self):
        move = input('Enter your move: ')
        
        self.counter_moves = move.split()
        

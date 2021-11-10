

class Player:
    def __init__(self):
        self.name = "player"
    
    
class Human(Player):
    def set_move(self):
        move = input('Enter your move: ')
        
        self.counter_moves = move.split()
        

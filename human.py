from player import Player
from time import sleep
gestures = ["Rock", "Paper", "scissors", "Lizard", "Spock"]

class Human(Player):
    
    def __init__(self):
        super().__init__()
    

    def choose_gesture(self):
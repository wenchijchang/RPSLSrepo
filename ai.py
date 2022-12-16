import random
from player import Player
from time import sleep
gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

class AI(Player):

    def __init__(self):
        super().__init__()
        self.name = "Computer"


    def choose_gesture(self):
        self.choose_gesture = random.choice(gestures)
        sleep(1)
        print(f"{self.name} has picked {self.choose_gesture}")




import random
from player import Player
from time import sleep
gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

class AI(Player):

    def __init__(self):
        super().__init__()
        self.name = "Computer"


    def choose_gesture(self):
        self.user_input = random.choice(gestures)
        sleep(1)
        print(f"{self.name} has picked {self.user_input}")
        return self.user_input



from player import Player
from time import sleep
gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

class Human(Player):
    
    def __init__(self):
        super().__init__()
        self.name = " "

    def choose_gesture(self):
        valid_gesture = False
        while valid_gesture == False:
            self.user_input = int(input("Please enter your gesture: "))
            if self.user_input == 0 or self.user_input == 1 or self.user_input == 2 or self.user_input == 3 or self.user_input == 4:
                sleep(1)
                print(self.name + " " + "has picked" + " " + gestures[int(self.user_input)])
                valid_gesture = True
            else:
                print("Invalid entry, please try again")
                valid_gesture = False
            return str(gestures[int(self.user_input)])
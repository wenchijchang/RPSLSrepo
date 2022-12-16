from time import sleep
from ai import AI
from human import Human


class Game:

    def __init__(self):
        self.player_one = " "
        self.player_two = " "
    
    def greeting(self):
        print("Welcome to Rock Paper Scissors Lizard Spock\n")
        sleep(1)
        print("Each match will be best of three games.\nPlease use the number keys to enter your selection.\n")
        sleep(1)

    def rules(self):
        print("Rock crushes Scissors")
        sleep(1)
        print("Scissors cuts Paper")
        sleep(1)
        print("Paper covers Rock")
        sleep(1)
        print("Rock crushes Lizard")
        sleep(1)
        print("Lizard poisons Spock")
        sleep(1)
        print("Spock smashes Scissors")
        sleep(1)
        print("Scissors decapitates Lizard")
        sleep(1)
        print("Lizard eats Paper")
        sleep(1)
        print("Paper disproves Spock")
        sleep(1)
        print("Spock vaporizes Rock")
        sleep(1)
        print("\n")

    def number_of_player(self):
        user_input = int(input("How many players? Please enter 1 or 2: "))
        if user_input == 2:
            self.player_one = Human()
            self.player_one.name = "Player one"
            self.player_two = Human()
            self.player_two.name = "Player two"
        elif user_input == 1:
            self.player_one = Human()
            self.player_one.name = "Player one"
            self.player_two = AI()
        else:
            print("Invalid entry, please try again")
            self.number_of_player()

    def gesture_options(self):
        print("\n")
        sleep(1)
        print("Enter 0 for Rock")
        sleep(1)
        print("Enter 1 for Paper")
        sleep(1)
        print("Enter 2 for Scissors")
        sleep(1)
        print("Enter 3 for Lizard")
        sleep(1)
        print("Enter 4 for Spock")
        sleep(1)
        print("\n")

    def play_game(self):
        Round = 1
        while Round < 4:
            self.player_one.user_input = self.player_one.choose_gesture()
            self.player_two.user_input = self.player_two.choose_gesture()
            if self.player_one.user_input == self.player_two.user_input:
                print("It's a draw!")
            elif self.player_one.user_input == "Rock" and (self.player_two.user_input == "Scissors" and "Lizard") or self.player_one.user_input == "Paper" and (self.player_two.user_input == "Rock" and "Spock") or self.player_one.user_input == "Scissors" and (self.player_two.user_input == "Lizard" and "Paper") or self.player_one.user_input == "Lizard" and (self.player_two.user_input == "Paper" and "Spock") or self.player_one.user_input == "Spock" and (self.player_two.user_input == "Scissors" and "Rock"):
                print(f"{self.player_one.name} wins!")
                self.player_one.score += 1
            elif self.player_two.user_input == "Rock" and (self.player_one.user_input == "Scissors" and "Lizard") or self.player_two.user_input == "Paper" and (self.player_one.user_input == "Rock" and "Spock") or self.player_two.user_input == "Scissors" and (self.player_one.user_input == "Lizard" and "Paper") or self.player_two.user_input == "Lizard" and (self.player_one.user_input == "Paper" and "Spock") or self.player_two.user_input == "Spock" and (self.player_one.user_input == "Scissors" and "Rock"):
                print(f"{self.player_two.name} wins!")
                self.player_two.score += 1
            Round += 1
            print("\n")
            print("\n")
        
    # def winner(self): 
    #     if self.player_one.score > self.player_two.score:
    #         print(f"{self.player_one.name} wins best of 3!")
    #     else:
    #         print(f"{self.player_two} wins best of 3!")
    #     user_input = input("Do you want to play again? Please enter Y/N: ")
    #     if user_input == "Y":
    #         self.run_game()
    #     else:
    #         print("Thank you for playing. Hope you had fun!")


    def run_game(self):
        # self.greeting()
        # self.rules()
        self.number_of_player()
        self.gesture_options()
        self.play_game()

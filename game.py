from time import sleep


class Game:

    def __init__(self):
        Round = 0
        self.player_one = " "
        self.play_two = " "
        # self.select_players()
    
    def greeting(self):
        print("Welcome to Rock Paper Scissors Lizard Spock\n")
        sleep(2)
        print("Each match will be best of three games.\nPlease use the number keys to enter your selection.\n")
        sleep(2)

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

    def run_game(self):
        self.greeting()
        self.rules()



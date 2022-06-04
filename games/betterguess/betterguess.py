import random as r

class BetterGuess:
    def __init__(self, max_number):
        super().__init__()
        self.max_number = max_number
        self.max_guesses = max_number / 10 + 2
        self.acutal_number = -1
        self.won = False

    def play_game(self):
        current_val = int(input("Pick a number between 1 and " + self.max_number))
        current_guesses = 0

        while current_guesses < self.max_guesses:
            current_guesses += 1
            if current_val == self.acutal_number:
                self.won = True
                break

        if not self.won:
            print("You lost. The actual number was", self.acutal_number)
        else:
            print("You won!")
import random as r

class BetterGuess:
    def __init__(self, max_number):
        super().__init__()
        self.max_number = max_number
        self.max_guesses = max_number / 10 + 2
        self.acutal_number = -1
        self.won = False

    def play_game(self):
        current_guesses = 0
        self.acutal_number = r.randint(1, self.max_number)
        while current_guesses < self.max_guesses:
            scurrent_val = input("Pick a number between 1 and " + str(self.max_number) + ": ")
            current_val = int(scurrent_val)
            current_guesses += 1
            if current_val == self.acutal_number:
                self.won = True
                break
            elif current_val < self.acutal_number:
                print("Think higher")
            else:
                print("Think lower")
            print("You have", str(self.max_guesses - current_guesses), "left")

        if not self.won:
            print("You lost. The actual number was", str(self.acutal_number))
        else:
            print("You won!")

g = BetterGuess(100)
g.play_game()
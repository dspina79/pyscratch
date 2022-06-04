import random as r

smax_num = input("Enter the max number to guess: ")
max_num = int(smax_num)

MAX_GUESSES = max_num / 10 + 5
current_guesses = 0

current_random = r.randint(1, max_num)
won = False
while current_guesses < MAX_GUESSES:
    current_guess = int(input("Pick a number between 1 and " + smax_num + ": "))
    if current_guess == current_random:
        print('You won!')
        won = True
        break
    else:
        current_guesses += 1
        guesses_Left = MAX_GUESSES - current_guesses
        print("You have", guesses_Left, "guesses left")

if not won:
    print("You lost. Sorry. The number was", current_random)


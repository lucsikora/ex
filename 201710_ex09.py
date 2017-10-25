# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 25th October, 2017
#
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low,
# too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
a = random.randint(1,9)
tries = 0
print("===== GUESS MY NUMBER =====\nTo end it type 'exit'")
while True:
    try:
        user_guess = input("Guess what number between 1 and 9 I'm thinking off: ")
        if user_guess == "exit":
            break

        tries += 1
        user_choice = int(user_guess)
    except ValueError:
        print("I was asking about number")
        continue
    if user_choice < a:
        print("Too small")
    elif user_choice > a:
        print("Too big")
    elif user_choice == a:
        print("That's Right!")
        print("Won in: ", tries, " tries")
        break
    else:
        print("That's not a number I've been asking. Try again")
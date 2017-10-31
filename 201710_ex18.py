# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 31st October, 2017
#
#
# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user
# guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly
# in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user
# makes throughout teh game and tell the user at the end.
#
# Say the number generated by the computer is 1038. An example interaction could look like this:
#
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...
#
# Until the user guesses the number.
import random

def gen_numb(size):
    return random.sample([1,2,3,4,5,6,7,8,9,0], size)


def get_usr_input():
    while True:
        usr_input = list(str(input("Write 4 digit number: ")))
        if len(usr_input) > 4:
            print("We only need 4 digits so we will use: " ,usr_input[0:4])
        elif len(usr_input) < 4:
            print("We need more digits")
            usr_input = list(str(input("Write 4 digit number: ")))
        usr_guess = list(map(int, usr_input[0:4]))
        return usr_guess


def compare_numbers(generated_number, usr_guess):
    cow = 0
    bull = 0
    for i in range(0, len(usr_guess)):
        if usr_guess[i] in generated_number and usr_guess[i] == generated_number[i]:
            cow += 1
        elif usr_guess[i] in generated_number and not usr_guess[i] == generated_number[i]:
            bull += 1
    if cow == 4:
        print("You Won!")
        return True
    else:
        print("You have ", cow, " Cows and ", bull, " Bulls")
        return False



generated_number = list(gen_numb(4))
print(generated_number)
print(" ===== GUESS MY NUMBER =====")
print("For every correct digit you got a bull, for every correct digit and its position you get a cow!")

while not compare_numbers(generated_number, get_usr_input()):
    print("Keep guessing")






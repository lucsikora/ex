# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 25th October, 2017
#
# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations
# to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
#     Rock beats scissors
#     Scissors beats paper
#     Paper beats rock

import random
print("Hi, lets play Rock-Paper-Scissors. To STOP it you have to win :)")
moves = ["rock", "paper", "scissors"]

while True:
    player_choice = input("Choose you move: 'rock', 'paper' or 'scissors': ")
    computer_choice = random.choice(moves)
    print("You choose: ", player_choice)
    print("Computer generated: ", computer_choice)

    if player_choice in moves:
        if player_choice == "rock" and computer_choice == "scissors":
            print("Player Wins!!")
            break
        elif player_choice == "paper" and computer_choice == "rock":
            print("Player Wins!!")
            break
        elif player_choice == "scissors" and computer_choice == "rock":
            print("Player Wins!!")
            break
        elif player_choice == computer_choice:
            print("We think alike, lets try again")
        else:
            print("Computer Won! All Hail The Machines!!")
    else:
        print("Please type correctly your move")
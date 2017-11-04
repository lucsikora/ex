# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 4th November, 2017
#
#
# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
#
# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number
# between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high,
# too low, or your number.
#
# At the end of this exchange, your program should print out how many guesses it took to get your number.
#
# As the writer of this program, you will have to choose how your program will strategically guess.
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit
# the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right
# in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program,
# try to find the optimal strategy!
# (We’ll talk about what is the optimal one next week with the solution.)

import math


def main():
    print("LETS PLAY A LITTLE GAME.\n Think about number between 1 and 100, I will try to guess it")
    lowest = 1
    highest = 100
    counter = 1
    while True:
        num_range = list(range(lowest-1, highest+1))
        num = num_range[math.floor(len(num_range)/2)]
        print("The number you're thinking is:", num)
        usr_res = input("Choose command [lower][higher][yes][exit]: ")

        if usr_res == 'lower':
            highest = num
        elif usr_res == 'higher':
            lowest = num
        elif usr_res == 'yes':
            print("Computer guessed your number:", num, "after", counter, "tries")
            break
        elif usr_res == 'exit':
            break

        counter += 1

if __name__ == "__main__":
    main()

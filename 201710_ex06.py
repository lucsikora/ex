# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 25th October, 2017
#
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

a = input("Hi, Please give me random word: ")
b = a[::-1]

if a == b:
    print("Congratulation! It's a Palindrome!")
else:
    print("Ohhh, that's not a palindrone type of word, please try again")
# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 27th October, 2017
#
#
# Write a program (using functions!) that asks the user for a long string containing multiple words.
#  Print back to the user the same string, except with the words in backwards order.
#  For example, say I type the string:
#   My name is Michele
#
# Then I would see the string:
#   Michele is name My
#
# shown back to me.

print("TIME TO REVERSE SOME WORDS !!")
def get_string():
    string = input("Hi, Please write random sentence with few words: ")
    return string


def reverse_words(x):
    splited_string = x.split()
    final_string = " ".join(splited_string[::-1])
    return final_string

print(reverse_words(get_string()))
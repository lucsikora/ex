# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 28th October, 2017
#
#
# Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns (then prints)
# an appropriate boolean.
#
# Extras:
#
#     Use binary search.


import random

def check_list(l, n):
    if n in l:
        print("It's in the list")
        return True
    else:
        print("It's NOT in the list")
        return False

def get_info():
    # user_list = [i for i in range(random.randrange(0, 1000))]
    # print(user_list)
    # user_list = (input("Please write a list of numbers: ")).split(' ')
    user_int_list = [int(x) for x in user_list]
    if user_list == "":
        user_int_list = [i for i in range(random.randrange(0, 1000))]
        # print(user_int_list)
    user_number = int(input("Please write a number your're looking for in a list: "))
    return user_int_list, user_number


if __name__ == "__main__":
    l, n = get_info()
    check_list(l,n)
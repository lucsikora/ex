# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 27th October, 2017
#
#
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
#  list minus all the duplicates.
#
# Extras:
#
#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#     Go back and do Exercise 5 using sets, and write the solution for that in a different function.

import random

def gen_list():
    a = [random.randrange(1, 30) for _ in range(0, random.randint(1,20))]
    # a = [1 ,2 ,3, 5, 6, 3, 4, 1]
    return a

def conv_list2set(lis):
    return set(lis)

generated_list = gen_list()
print("Generated list: ", generated_list)
print("Created set: ", conv_list2set(generated_list))


# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 27th October, 2017
#
#
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

def list_edges(lista):
    return [lista[0], lista[len(lista)-1]]


a = [5, 10, 15, 20, 25]
print(list_edges(a))
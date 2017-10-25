# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 25th October, 2017
#
#
# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# 1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


# Basic task
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i < 5:
        print(i)


# Extra 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i < 5:
        b.append(i)
print(b)


# Extra 2
# Hint: http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [item for item in a if item < 5]
print(b)


# Extra 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = input("Write numers lower than: ")
b = [item for item in a if item < num]
print(b)
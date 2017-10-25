# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 25th October, 2017
#
#
# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
#  1.  Randomly generate two lists to test this
#  2.  Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)


# Extras 1
import random
a = random.sample(range(100), 20)
b = random.sample(range(100), 20)
c = []
for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)


# Extras 2
a = [random.randrange(1,10) for _ in range(0, random.randint(1,20))]
b = [random.randrange(1,10) for _ in range(0, random.randint(1,20))]
c = []
c = [i for i in a if (i in b and i not in c)] # Repeates are not excluded - not sure why
print(a)
print(b)
print(c)
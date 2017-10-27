# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 27th October, 2017
#
#
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers
# in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
#     The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)


# Not elegant version

def get_number():
    num = int(input("Please specify how many Fibonnaci numbers should I generate: "))
    return num

a = []
for i in range(1, get_number()):
    if len(a) < 1:
        a.append(i)
    elif len(a) == 1:
        a.append(1)
    elif len(a) >= 2:
        a.append(a[-1] + a[-2])

print(a)
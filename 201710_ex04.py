# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 25th October, 2017
#
#
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

print("Hi, I will tell you all divisors of you number.")
num = input("Please choose a number: ")

for i in range(0,num):
    if num % i == 0:
        print(i)
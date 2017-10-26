# practicepython.py
#
# Solution by: Lukasz Sikora
# Date: 26th October, 2017
#
#
# CAsk the user for a number and determine whether the number is prime or not. (For those who have forgotten,
# a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.


def get_number(message):
    return int(input(message))

def is_prime(num):
    for i in range(2, num-1):
        print(i)
        if num % i == 0:
            return 'not a prime'
        else:
            return 'prime'

print("Hi, I will tell you if you number is a prime")
number = get_number("Please choose a number: ")
print("Your number: ", number, " is ", is_prime(number))


# Exercise 31
# Level 1
# written by: Vince Mao
# last modified: 2019.5.3
# Description:
# Define a function that can accept an integer number as input and print
# "It is an even number." if the number is even, otherwise print "It is an odd number.".
#
# Hint:
# Use the % operator to check if a number is even or odd.
#
# Pseudocode:
# 1. Define a function that takes a number and returns whether it is even or odd.


def even_or_odd(number):
    if int(number):
        if number % 2 == 0:
            return "It is an even number."
        else:
            return "It is an odd number."


print even_or_odd(12)
print even_or_odd(13)

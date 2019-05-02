# Exercise 28
# Level 1
# written by: Vince Mao
# last modified: 2019.5.2
# Description:
# Define a function that takes two integer numbers in string format and returns the sum of the two values.
#
# Hint:
# Use the int() method.
#
# Pseudocode:
# 1. Define a function that takes two integer values and returns the calculated sum.


def add_two_string_nums(a, b):
    if str(a) and str(b):
        return int(a) + int(b)
    else:
        return "Two integers as strings are needed!"


print add_two_string_nums("4", "6")

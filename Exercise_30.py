# Exercise 30
# Level 1
# written by: Vince Mao
# last modified: 2019.5.2
# Description:
# Define a function that takes two strings as input and returns the longer string.
# If the two strings are the same length, then the function should print both strings line by line.
#
# Hint:
# Use the len() function to determine the length of a string.
#
# Pseudocode:
# 1. Define a function that takes two strings and returns the longer string or both if the strings are equal in length.


def compare_two_strings(a, b):
    if str(a) and str(b):
        if len(a) > len(b):
            return a
        elif len(a) < len(b):
            return b
        else:
            return a + "\n" + b
    else:
        return "Two strings are needed!"


print compare_two_strings("12", "3")
print compare_two_strings("4", "6")
print compare_two_strings("3", "12")

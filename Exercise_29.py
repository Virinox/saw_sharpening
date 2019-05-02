# Exercise 29
# Level 1
# written by: Vince Mao
# last modified: 2019.5.2
# Description:
# Define a function that takes two strings and returns the concatenated result.
#
# Hint:
# Use "+" to add strings together.
#
# Pseudocode:
# 1. Define a function that takes two strings and returns the concatenated result.


def combine_two_strings(a, b):
    if str(a) and str(b):
        return a + b
    else:
        return "Two strings are needed!"


print combine_two_strings("4", "6")

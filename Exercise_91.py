# Exercise 91
# Level 1
# written by: Vince Mao
# last modified: 2019.6.9
# Description:
# Given the list [12,24,35,24,88,120,155,88,120,155], write a program
# to create a list without duplicate elements.
#
# Hint:
# Use set() to create list with no duplicates.
#
# Pseudocode:
# 1. Initialize the list.
# 2. Print the result using set().

test = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
result = set(test)
print list(result)

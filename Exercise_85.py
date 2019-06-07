# Exercise 85
# Level 1
# written by: Vince Mao
# last modified: 2019.6.7
# Description:
# Please write a program to print the list after removing numbers
# which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
#
# Hint:
# Use list comprehension to delete elements from a list.
#
# Pseudocode:
# 1. Initialize the list.
# 2. Print the result of iterating through the list that does not allow
#     numbers divisible by 5 and numbers that are divisible by 7.

test = [12, 24, 35, 70, 88, 120, 155]

print [x for x in test if x % 5 != 0 and x % 7 != 0]

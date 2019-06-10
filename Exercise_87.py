# Exercise 87
# Level 1
# written by: Vince Mao
# last modified: 2019.6.9
# Description:
# Please write a program to generate a 3*5*8 3D array with all elements equal to 0.
#
# Hint:
# Use list comprehension to create an array.
#
# Pseudocode:
# 1. Print the list comprehension from 8 to 5 to 3 in k, j, and i dimensions.

print [[[0 for k in range(8)]for j in range(5)]for i in range(3)]

# Exercise 90
# Level 1
# written by: Vince Mao
# last modified: 2019.6.9
# Description:
# Given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program
# to create a list with the elements from both lists.
#
# Hint:
# Use set() and "&" to do the set intersection operation.
#
# Pseudocode:
# 1. Initialize the lists.
# 2. Print the result using set() and "&".

test1 = [12, 24, 35, 70, 88, 120, 155]
test2 = [1, 3, 6, 78, 35, 55]
set1 = set(test1)
set2 = set(test2)

print list(set1 & set2)
print list(set1.intersection(set2))

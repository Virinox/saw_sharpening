# Exercise 88
# Level 1
# written by: Vince Mao
# last modified: 2019.6.9
# Description:
# Please write a program to print the list after removing the
# 0th, 4th, 5th numbers in [12,24,35,70,88,120,155].
#
# Hint:
# Use list comprehension to delete elements from a list.
# Use the enumerate() function to get the (index, value) tuple.
#
# Pseudocode:
# 1. Initialize the list.
# 2. Enumerate the list.
# 3. Print the result that is not in the 0th, 4th, and 5th indices.

test = [12, 24, 35, 70, 88, 120, 155]
result = []
for x, y in enumerate(test):
    if x not in [0, 4, 5]:
        result.append(y)

print result

# Exercise 89
# Level 1
# written by: Vince Mao
# last modified: 2019.6.9
# Description:
# Please write a program to print the list after removing the value 24
# from the list [12,24,35,70,88,120,155].
#
# Hint:
# Use list comprehension to omit elements from a list.
#
# Pseudocode:
# 1. Initialize the list.
# 2. Print the result without the value.

test = [12, 24, 35, 70, 88, 120, 155]
result = []
for x in range(len(test)):
    if test[x] != 24:
        result.append(test[x])

print result
print [x for x in test if x != 24]

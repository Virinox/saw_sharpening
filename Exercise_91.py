# Exercise 91
# Level 1
# written by: Vince Mao
# last modified: 2019.6.9
# Description:
# Given the list [12,24,35,24,88,120,155,88,120,155], write a program
# to create a list without duplicate elements. Ensure the order of the
# list is preserved.
#
# Hint:
# Use set() to create list with no duplicates.
#
# Pseudocode:
# 1. Initialize the list.
# 2. Print the result using set().
# 3. Use this set on the original list to generate the new list.

test = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
check = list(set(test))
result = []

for i in range(len(test)):
    if test[i] in check and test[i] not in result:
        result.append(test[i])
        
print check
print result


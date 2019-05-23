# Exercise 69
# Level 1
# written by: Vince Mao
# last modified: 2019.5.22
# Description:
# Please write assert statements to verify that every number in the list [2,4,6,8] is even.
#
# Hint:
# Use the assert method to make an assertion.
#
# Pseudocode:
# 1. Define the list.
# 2. Use a for loop to check if every element in the list is even.


check = [2, 4, 6, 8]

for i in range(len(check)):
    assert check[i] % 2 == 0

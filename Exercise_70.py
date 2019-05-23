# Exercise 70
# Level 1
# written by: Vince Mao
# last modified: 2019.5.22
# Description:
# Please write a program which accepts basic math expressions from the console and print the evaluation result.
#
# Example:
# Given the following input:
# 35 + 3
# The output should be:
# 38
#
# Hint:
# Use the eval method to do a calculation.
#
# Pseudocode:
# 1. Test inputs using eval().


test = raw_input("Please enter a calculation: ")
print eval(test)

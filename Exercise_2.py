# Exercise 2
# written by: Vince Mao
# last modified: 2019.4.18
# Description:
# Write a program which can compute the factorial of a given number.
# The result should be printed on a single line.
# Example: Suppose the following input is supplied to the program:
# 8
# The result should be:
# 40320
#
# Hint:
# The input should be assumed to be a console input.
#
# Pseudocode:
# 1. Pass the value in from an external variable
# 2. Define the base case of the factorial
# 3. Return the recursive call of the product of the current value with the previous value


def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)


entry = raw_input("Enter a number: ")
print factorial(int(entry))

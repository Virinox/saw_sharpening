# Exercise 64
# Level 1
# written by: Vince Mao
# last modified: 2019.5.15
# Description:
# Write a program to compute the following:
#
# f(n)=f(n-1)+100 when n>0
# and f(0)=0
#
# for a given n input via console (n>0).
#
# Example:
# Given the following input:
# 5
# The output should be:
# 500
#
# Hint:
# The data should be assumed to be a console input.
# Use recursion.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for raw input from the console.
# 4. Instantiate the function for going through the string and calculate the given equation.
# 5. Call the recursive function based on input.


class RecursionCalc:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please enter a number: ")


def process(count):
    if str(count).isdigit():
        current = int(count)
        if current == 0:
            return 0
        else:
            return process(current - 1) + 100
    else:
        return "Not a number!"


test = RecursionCalc()
test.input()
print process(test.entry)

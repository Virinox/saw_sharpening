# Exercise 63
# Level 1
# written by: Vince Mao
# last modified: 2019.5.15
# Description:
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input via console (n>0).
#
# Example:
# Given the following input:
# 5
# The output should be:
# 3.55
#
# Hint:
# The data should be assumed to be a console input.
# Use float() to convert an integer to a float.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for raw input from the console.
# 4. Instantiate the method for going through the string and calculate the given equation.
# 5. Return the result in the form of a float.


class FracCalc:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please enter a number: ")

    def process(self):
        result = 0
        if self.entry.isdigit():
            for i in range(1, int(self.entry) + 1):
                equation = float(i) / float(i + 1)
                result += equation
            return result
        else:
            return "Not a number!"


test = FracCalc()
test.input()
print test.process()

# Exercise 6
# Level 2
# written by: Vince Mao
# last modified: 2019.4.21
# Description:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# The following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable containing values supplied to your program in a comma-separated sequence.
# Example:
# Given the following list:
# 100,150,180
# The output of the program should be:
# 18,22,24
#
# Hints:
# If the output received is in decimal form, it should be rounded to its nearest value.
# For example, if the output received is 26.0, it should be printed as 26.
# The data should be assumed to be a console input.
#
# Pseudocode:
# 1. Import the math package for Python.
# 2. Implement a class for the program.
# 3. Initialize C and H to their values in the __init__ method.
# 4. Define a method to get the raw input string for D.
# 5. Return the result in integer form by rounding after the calculation.


from math import sqrt


class Calculate:
    def __init__(self):
        self.C = 50
        self.H = 30
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please input a comma-separated sequence of numbers for calculation: ")

    def calculate(self):
        solution = []
        if self.entry is not None:
            d = self.entry.split(',')
            for i in range(len(d)):
                if not d[i].isdigit():
                    return "Error in list input!"
                else:
                    solution.append(int(round(sqrt((2 * self.C * int(d[i]) / self.H)))))

        return solution


test = Calculate()
test.input()
print test.calculate()

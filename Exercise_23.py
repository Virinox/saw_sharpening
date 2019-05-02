# Exercise 23
# Level 1
# written by: Vince Mao
# last modified: 2019.5.2
# Description:
# Write a method to calculate the square of a number.
#
# Hint:
# The data should be assumed to be a console input.
# Use the ** operator.
#
# Pseudocode:
# 1. Instantiate a class for the calculation.
# 2. Instantiate the method that requests the input.
# 3. Instantiate the method for returning the square.


class Square:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please enter a number: ")

    def generate(self):
        return int(self.entry) ** 2


test = Square()
test.input()
print test.generate()

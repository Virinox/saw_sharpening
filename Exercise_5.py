# Exercise 5
# Level 1
# written by: Vince Mao
# last modified: 2019.4.20
# Description:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also include a simple test function to test the class methods.
#
# Hints:
# Use __init__ method to construct some parameters
#
# Pseudocode:
# 1. Initialize a class to get the raw input
# 2. Assign the string to the getString method
# 3. Define the printString method to capitalize the string.


class String:
    def __init__(self):
        self.entry = ""

    def getString(self):
        self.entry = raw_input("Please enter a string: ")
        return self.entry

    def printString(self):
        return self.entry.upper()


test = String()
print test.printString()

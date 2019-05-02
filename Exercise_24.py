# Exercise 24
# Level 1
# written by: Vince Mao
# last modified: 2019.5.2
# Description:
# Python has many built-in functions. If you don't know how to use a function, you can read the
# documentation online or in books. However, Python has a built-in document function for all built-in functions.
#
# Write a program to print the documentation for built-in Python functions (i.e., abs(), int(), raw_input())
# Add documentation for your own function.
#
# Hint:
# The data should be assumed to be a console input.
# Use the __doc__ method.
#
# Pseudocode:
# 1. Instantiate a class.
# 2. Instantiate a method and add some documentation for it.
# 3. Print out the documentation for the method.
# 4. Print out the documentation for a built-in Python function.


class Document:
    def __init__(self):
        self.entry = ""

    def input(self):
        """Asks the user for an input from the console.
        
Returns the input.
        """
        self.entry = raw_input("Please enter a known Python function: ")
        return self.entry


test = Document()
print test.input.__doc__
print abs.__doc__

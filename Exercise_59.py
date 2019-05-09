# Exercise 59
# Level 2
# written by: Vince Mao
# last modified: 2019.5.8
# Description:
# Write a program which accepts a sequence of words separated by whitespace as input
# to print the words composed of digits only.
#
# Example:
# Given the following input:
# 2 cats and 3 dogs.
# The output should be:
# ['2', '3']
#
# Hint:
# The data should be assumed to be a console input.
# Use re.findall() to find all substrings using regex.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for raw input from the console.
# 4. Instantiate the method for going through the string and determining all numbers using re.findall().
# 5. Return the list of numbers based on the search result.


import re


class FindNums:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please enter a sentence containing numbers: ")

    def process(self):
        check = re.findall("\d", self.entry)
        return check


test = FindNums()
test.input()
print test.process()

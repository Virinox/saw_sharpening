# Exercise 9
# Level 2
# written by: Vince Mao
# last modified: 2019.4.22
# Description:
# Write a program that accepts sequence of lines as input and prints the lines after
# capitalizing all characters.
#
# Example:
# Given the following inputs:
# Hello world
# Practice makes perfect
# The output of the program should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
#
# Hint:
# The data should be assumed to be a console input.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for getting multiple line input from the console for the word list.
# 4. Instantiate the method for generating the string with all letters capitalized.
# 5. Return the resulting modified string.


import sys


class Capitalize:
    def __init__(self):
        self.entry = ""

    def input(self):
        print "Please input a string of words: "
        self.entry = sys.stdin.readlines()

    def generate(self):
        solution = []
        if self.entry is not None:
            for line in self.entry:
                solution.append(str(line).upper())

        return "".join(solution)


test = Capitalize()
test.input()
print test.generate()

# Exercise 8
# Level 2
# written by: Vince Mao
# last modified: 2019.4.22
# Description:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a
# comma-separated sequence after sorting them alphabetically.
#
# Example:
# Given the following inputs:
# without,hello,bag,world
# The output of the program should be:
# bag,hello,without,world
#
# Hint:
# The data should be assumed to be a console input.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for raw input from the console for the word list.
# 4. Instantiate the method for generating the array with the sorted elements.
# 5. Return the resulting array.


class Alpha:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please input a comma-separated list of words: ")

    def generate(self):
        solution = ""
        array = ""
        if self.entry is not None:
            array = self.entry.split(',')
            array.sort()

        for i in range(len(array)):
            if i != len(array)-1:
                solution += array[i] + ","
            else:
                solution += array[i]

        return solution


test = Alpha()
test.input()
print test.generate()

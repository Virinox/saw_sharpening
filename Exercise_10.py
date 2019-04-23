# Exercise 10
# Level 2
# written by: Vince Mao
# last modified: 2019.4.22
# Description:
# Write a program that accepts a sequence of whitespace separated words as the input and prints
# the words after removing all duplicate words and sorting them alphanumerically.
#
# Example:
# Given the following input:
# hello world and practice makes perfect and hello world again
# The output of the program should be:
# again and hello makes perfect practice world
#
# Hint:
# The data should be assumed to be a console input.
# Use set method to remove duplicate data automatically and then use sorted() to sort the data.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for raw input from the console for the word list.
# 4. Instantiate the method for generating the list that parses all words for whitespace.
# 5. Use the set method to remove duplicates.
# 6. Return the sorted list.


class StringSort:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please input a string of words: ")

    def process(self):
        final = set()
        if self.entry is not None:
            solution = self.entry.split()
            for words in solution:
                final.add(words)
        return " ".join(sorted(final))


test = StringSort()
test.input()
print test.process()

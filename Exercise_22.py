# Exercise 22
# Level 3
# written by: Vince Mao
# last modified: 2019.5.2
# Description:
# Write a program to compute the frequency of the word occurrence from the input.
# The output should sort by key alphanumerically.
# Example:
# Given the following input:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# The output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
#
# Hint:
# The data should be assumed to be a console input.
#
# Pseudocode:
# 1. Instantiate a class for the word count.
# 2. Instantiate the method that requests the input.
# 3. Instantiate the method for parsing the input using whitespace and tallying word occurrences.
# 4. Add each element to a dictionary to keep track by going through the input once.
# 5. Sort the dictionary.
# 6. Print the word and number of occurrences.


class WordOccurrence:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please type in a sentence or a phrase: ")

    def generate(self):
        check = {}
        if self.entry is not None:
            for x, word in enumerate(self.entry.split()):
                if word in check:
                    check[word] += 1
                else:
                    check[word] = 1

            for i in sorted(check.keys()):
                print("%s:%d" % (i, check[i]))


test = WordOccurrence()
test.input()
test.generate()

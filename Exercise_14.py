# Exercise 14
# Level 2
# written by: Vince Mao
# last modified: 2019.4.27
# Description:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Example:
# Given the following input:
# Hello world!
# The output should be:
# UPPER CASE 1
# LOWER CASE 9
#
# Hint:
# The data should be assumed to be a console input.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for raw input from the console.
# 4. Instantiate the method for going through the string and counting lower and upper case letters.
# 5. Return the counts for lower and upper case letters.


class UpperLowerCount:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please enter a phrase or sentence containing lower and upper case letters: ")

    def process(self):
        result = {"UPPER": 0, "LOWER": 0}
        check = self.entry.split(" ")
        for word in check:
            for i in range(len(word)):
                if word[i].isupper():
                    result["UPPER"] += 1
                elif word[i].islower():
                    result["LOWER"] += 1
        final = "UPPER CASE " + str(result["UPPER"]) + "\n" + "LOWER CASE " + str(result["LOWER"])
        return final


test = UpperLowerCount()
test.input()
print test.process()

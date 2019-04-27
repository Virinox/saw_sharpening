# Exercise 13
# Level 2
# written by: Vince Mao
# last modified: 2019.4.27
# Description:
# Write a program that accepts a sentence and calculate the number of letters and digits.

# Example:
# Given the following input:
# hello world! 123
# The output should be:
# LETTERS 10
# DIGITS 3
#
# Hint:
# The data should be assumed to be a console input.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for raw input from the console.
# 4. Instantiate the method for going through the string and counting letters and digits.
# 5. Return the counts for letters and digits.


class AlphaNumCount:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please enter a phrase or sentence that contains numbers and letters: ")

    def process(self):
        result = {"LETTERS":0, "DIGITS": 0}
        check = self.entry.split(" ")
        for word in check:
            for i in range(len(word)):
                if word[i].isalpha():
                    result["LETTERS"] += 1
                elif word[i].isdigit():
                    result["DIGITS"] += 1
        final = "LETTERS " + str(result["LETTERS"]) + "\n" + "DIGITS " + str(result["DIGITS"])
        return final


test = AlphaNumCount()
test.input()
print test.process()

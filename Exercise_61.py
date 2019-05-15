# Exercise 61
# Level 1
# written by: Vince Mao
# last modified: 2019.5.14
# Description:
# Write a program to read an ASCII string and convert it into a unicode string encoded by utf-8.
#
# Hint:
# Use the unicode() function to convert.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for raw input from the console.
# 4. Return the unicode string.


class AsciiUnicode:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please enter an ASCII string: ")

    def process(self):
        return unicode(self.entry, "utf-8")


test = AsciiUnicode()
test.input()
print test.process()

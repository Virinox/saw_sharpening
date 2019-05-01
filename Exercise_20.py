# Exercise 20
# Level 3
# written by: Vince Mao
# last modified: 2019.4.30
# Description:
# Define a class with a generator that can iterate the numbers that are divisible by 7 in a given range between 0 and n.
# Your program should accept a multiple line input of comma-separated tuples.
#
# Hint:
# The data should be assumed to be a console input.
# Consider using the yield method.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Instantiate the method that requests the range input.
# 3. Instantiate the method for generating the output.
# 4. Use a loop to go through the numbers in the range and yield any number that is divisible by 7.


class SevenMod:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please enter a number to define range for generating all numbers divisible by 7: ")

    def generate(self):
        i = 0
        while i in range(int(self.entry) + 1):
            if i % 7 == 0:
                yield i
            i += 1


test = SevenMod()
test.input()

for j in test.generate():
    print j

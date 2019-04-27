# Exercise 13
# Level 2
# written by: Vince Mao
# last modified: 2019.4.27
# Description:
# Write a program that computes the value of a + aa + aaa + aaaa with a given digit as the value of a.

# Example:
# Given the following input:
# 9
# The output should be:
# 11106
#
# Hint:
# The data should be assumed to be a console input.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Instantiate the method for raw input from the console.
# 3. Instantiate the method for generating the equation
# 4. Return the result


class SumUp:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please input a digit between 0 and 9: ")

    def process(self):
        result = 0
        if self.entry.isdigit():
            for digit in range(1, 5):
                result += int(str(self.entry) * digit)
        else:
            return "Input is not a digit!"
        return result


test = SumUp()
test.input()
print test.process()

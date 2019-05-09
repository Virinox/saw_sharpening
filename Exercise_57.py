# Exercise 57
# Level 2
# written by: Vince Mao
# last modified: 2019.5.8
# Description:
# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write a program to print the user name of a given email address.
# Both the user name and company name are composed of letters only.
#
# Example:
# Given the following input:
# john@google.com
# The output should be:
# john
#
# Hint:
# The data should be assumed to be a console input.
# Use \w to match letters.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Initialize an empty string in the init class.
# 3. Instantiate the method for raw input from the console.
# 4. Instantiate the method for going through the string and determining the user name portion of the address.
#    Either split using the "@" or use "\w" to match letters until you find the "@" character.
# 5. Return the user name.


import re


class UserName:
    def __init__(self):
        self.entry = ""

    def input(self):
        self.entry = raw_input("Please enter an email address: ")

    def process1(self):
        check = self.entry.split("@")

        return check[0]

    def process2(self):
        look = []
        cycle = str(self.entry)
        for i in range(len(cycle)):
            result = re.search('\w', cycle[i])
            if result:
                look.append(cycle[i])
            else:
                return ''.join(look)

    def process3(self):
        parse = "(\w+)@((\w+\.)+(com))"
        return re.match(parse, str(self.entry)).group(1)


test = UserName()
test.input()
print test.process1()
print test.process2()
print test.process3()

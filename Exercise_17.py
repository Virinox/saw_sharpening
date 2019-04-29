# Exercise 17
# Level 2
# written by: Vince Mao
# last modified: 2019.4.27
# Description:
# Write a program that computes the amount in a bank account based on a transaction log from console input.
# The transaction log should have the following format:
# D 100
# W 200
# "D" indicates a deposit while "W" indicates a withdrawal.
#
# The list is input by a sequence of comma-separated numbers.
#
# Example:
# Given the following inputs:
# D 300
# D 300
# W 200
# D 100
# The output should be:
# 500
#
# Hint:
# The data should be assumed to be a console input.
#
# Pseudocode:
# 1. Instantiate a class for the program.
# 2. Instantiate the method for multiple line input from the console.
# 3. Instantiate the method for determining the type of transaction and summing the current amount.
# 4. Return the current amount.

import sys


class Transaction:
    def __init__(self):
        self.entry = ""

    def input(self):
        print "Please input the transaction log: (D) for deposit, (W) for withdrawal"
        self.entry = sys.stdin.readlines()

    def process(self):
        account = 0
        if self.entry is not None:
            for line in self.entry:
                check = str(line).split()
                if not check[1].isdigit():
                    return "Transaction log error!"
                if check[0] == "D":
                    account += int(check[1])
                elif check[0] == "W":
                    account -= int(check[1])
                else:
                    return "Transaction log error!"
            if account < 0:
                return "Overdrawn!"
            else:
                return account


test = Transaction()
test.input()
print test.process()

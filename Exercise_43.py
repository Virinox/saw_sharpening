# Exercise 43
# Level 1
# written by: Vince Mao
# last modified: 2019.5.7
# Description:
# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes".
# Otherwise print "No".
#
# Hint:
# Use the if statement to determine if the condition is true or not
#
# Pseudocode:
# 1. Define a function to prompt a raw input.
# 2. Determine if the raw input fits any of the three inputs to return "Yes"
# 3. Else, print "No"


def check_yes():
    test = raw_input("Please type in yes: ")

    if test == "Yes" or test == "yes" or test == "YES":
        return "Yes"
    else:
        return "No"


print check_yes()

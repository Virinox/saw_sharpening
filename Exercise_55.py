# Exercise 55
# Level 1
# written by: Vince Mao
# last modified: 2019.5.8
# Description:
# Write a function to compute 5/0 and use try/except to catch the exceptions.
#
# Hint:
# Use the try/except methods to catch exceptions.
#
# Pseudocode:
# 1. Define a function to return the divide by zero calculation.
# 2. Try the function.
# 3. Except divide by zero statement.
# 4. Invoke finally to clean up the code regardless of the calculation.


def division_zero():
    return 5 / 0


try:
    division_zero()
except ZeroDivisionError:
    print "Divide by zero found!"
finally:
    print "Clean up the code."

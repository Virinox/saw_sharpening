# Exercise 56
# Level 2
# written by: Vince Mao
# last modified: 2019.5.8
# Description:
# Define a custom exception class which takes a string message as attribute.
#
# Hint:
# To define a custom exception, we need to define a class inherited from Exception.
#
# Pseudocode:
# 1. Define a class for the custom exception with Exception as the object to inherit the properties.
# 2. Add an argument in the __init__ method that takes a string argument.


class MyException(Exception):
    def __init__(self, exception):
        self.error = exception


error = MyException("Something is wrong!")

try:
    raise error
except MyException:
    print error
finally:
    print "Clean up the code."

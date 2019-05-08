# Exercise 49
# Level 1
# written by: Vince Mao
# last modified: 2019.5.8
# Description:
# Define a class named American that contains a static method called printNationality.
#
# Hint:
# Use the @staticmethod decorator to define a class static method.
#
# Pseudocode:
# 1. Instantiate a class called "American".
# 2. Include the @staticmethod decorator in the class.
# 3. Define the printNationality method to return the nationality.


class American:
    def __init__(self, nationality):
        self.nationality = nationality

    @staticmethod
    def print_nationality(nationality):
        return nationality


test = American("American")
print test.print_nationality("USA")

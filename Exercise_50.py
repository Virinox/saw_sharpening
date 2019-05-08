# Exercise 50
# Level 1
# written by: Vince Mao
# last modified: 2019.5.8
# Description:
# Define a class named American and its subclass NewYorker.
#
# Hint:
# Use the format class Subclass(ParentClass) to define a subclass.
#
# Pseudocode:
# 1. Instantiate a class called "American".
# 2. Instantiate the subclass NewYorker after the super class is instantiated.


class American(object):
    def __init__(self, nationality):
        self.nationality = nationality


class NewYorker(American):
    def __init__(self, nationality):
        super(NewYorker, self).__init__(nationality)


test = NewYorker("American")
print test.nationality

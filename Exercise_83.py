# Exercise 83
# Level 1
# written by: Vince Mao
# last modified: 2019.6.6
# Description:
# Please write a program to generate all sentences where the subject is in ["I", "You"],
# the verb is in ["Play", "Love"], and the object is in ["Hockey","Football"].
#
# Hint:
# Use the list[index] notation to get a element from a list.
#
# Pseudocode:
# 1. Initialize the subject, verb, and object lists.
# 2. Use nested for loops to generate all combinations of the three lists.

subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

sentence = ''
for i in subjects:
    for j in verbs:
        for k in objects:
            sentence = "%s %s %s." % (i, j, k)
            print sentence

# Exercise 84
# Level 1
# written by: Vince Mao
# last modified: 2019.6.7
# Description:
# Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].
#
# Hint:
# Use list comprehension to delete elements from a list.
#
# Pseudocode:
# 1. Initialize the list.
# 2. Iterate through the list and record the index of the numbers that are odd.
# 3. Iterate through the index list and delete the elements at the index. 
# 4. Account for the reduction in index in each iteration.
# 5. Print the resulting list.

test = [5, 6, 77, 45, 22, 12, 24]
test2 = test
even = []
count = 0

for i in range(len(test)):
    if int(test[i]) % 2 == 0:
        even.append(i)

for i in even:
    del test[i - count]
    count += 1

print test
print [x for x in test if x % 2 != 0]

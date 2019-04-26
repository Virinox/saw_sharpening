# Exercise 12
# Level 2
# written by: Vince Mao
# last modified: 2019.4.25
# Description:
# Write a program which will find all such numbers between 1000 and 3000 (both included) such that each digit
# of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
#
# Hint:
# The data should be assumed to be a console input.
#
# Pseudocode:
# 1. Initialize an empty list for the solution set.
# 2. Loop through all numbers in the range 1000 to 3001.
# 3. Loop through each digit of each number and check to see if they are even.
# 4. If not, break out of the loop.
# 5. Else if the loop has reached the end of the number, add that number in string format to the list.
# 6. Print the solution.

solution = []

for i in range(1000, 3001):
    for j in range(4):
        if int(str(i)[j]) % 2 != 0:
            break
        elif j == 3:
            solution.append(str(i))

print ', '.join(solution)

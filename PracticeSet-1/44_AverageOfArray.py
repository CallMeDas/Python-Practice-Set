'''Finding the Average of Numbers in an Array
Difficulty: Easy
Topics: Arrays, Mathematical Computations
Description: Write a program to calculate the average of numbers in an array.
Example:
Input: array = [1, 2, 3, 4, 5]
Output: 3
Explanation: The average of the numbers is (1 + 2 + 3 + 4 + 5) / 5 = 3.'''

def averageArray(n):
    s= 0
    for i in n:
        s += i
    return s/len(n)

print(averageArray([1, 2, 3, 4, 5]))
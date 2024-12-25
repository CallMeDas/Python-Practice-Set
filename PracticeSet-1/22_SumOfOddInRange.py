'''Calculating the Sum of Odd Numbers in a Range
Difficulty: Easy
Topics: Basic Programming, Mathematical Computations
Description: Write a program to find the sum of all odd numbers within a given range.
Example:
Input: range = [1, 10]
Output: 25
Explanation: The sum of odd numbers between 1 and 10 is 1 + 3 + 5 + 7 + 9 = 25.'''

def sumOddRange(start, end):
    sum = 0
    for i in range (start, end + 1):
        if i % 2 == 1:
            sum += i
    return sum

print(sumOddRange(1, 10))
'''Calculating the Sum of Even Numbers in a Range
Difficulty: Easy
Topics: Basic Programming, Mathematical Computations
Description: Write a program to find the sum of all even numbers within a given range.
Example:
Input: range = [1, 10]
Output: 30
Explanation: The sum of even numbers between 1 and 10 is 2 + 4 + 6 + 8 + 10 = 30.'''

def sumEvenRange(start, end):
    sum = 0
    for i in range (start, end + 1):
        if i % 2 == 0:
            sum += i
    return sum

print(sumEvenRange(1, 10))
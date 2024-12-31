'''Finding the Sum of Squares of Digits
Difficulty: Easy
Topics: Basic Programming, Mathematical Computations
Description: Write a program to find the sum of the squares of the digits of a number.
Example:
Input: number = 123
Output: 14
Explanation: The sum of the squares of digits is 1^2 + 2^2 + 3^2 = 14.'''

def sumSqrDigit(n):
    s= 0

    while n != 0:
        r = n % 10
        s = s + r * r
        n = n // 10
    return s


print(sumSqrDigit(123))
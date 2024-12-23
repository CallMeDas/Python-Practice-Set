'''Summing Digits of a Number
Difficulty: Easy
Topics: Basic Programming, Mathematical Computations
Description: Write a program to calculate the sum of digits of a number.
Example:
Input: number = 1234
Output: 10
Explanation: The sum of the digits 1 + 2 + 3 + 4 = 10.'''

def sumOfDigit(n):
    s = 0
    while n != 0:
        r = n % 10
        s  += r
        n = n // 10 
    return s



print(sumOfDigit(1235))
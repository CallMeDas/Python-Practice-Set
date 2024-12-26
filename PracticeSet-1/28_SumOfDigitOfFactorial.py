'''Finding the Sum of the Digits of the Factorial of a Number
Difficulty: Easy
Topics: Basic Programming, Mathematical Computations
Description: Write a program to find the sum of the digits of the factorial of a given number.
Example:
Input: number = 4
Output: 9
Explanation: The factorial of 4 is 24, and the sum of the digits (2 + 4) is 6.'''

def sumOfDigit(n):
    f = 1
    s = 0
    for i in range (1, n+1):
        f *= i
    
    while f != 0:
        r = f % 10
        s = s + r
        f = f // 10

    return s


print(sumOfDigit(4))
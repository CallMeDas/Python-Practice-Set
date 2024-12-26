'''Finding the Number of Digits in a Number
Difficulty: Easy
Topics: Basic Programming, Mathematical Computations
Description: Write a program to count the number of digits in a given number.
Example:
Input: number = 12345
Output: 5
Explanation: The number 12345 has 5 digits.'''

def countDigits(n):
    c = 0
    while n != 0:
        r = n % 10
        n = n // 10
        c += 1
    return c


print(countDigits(12345))


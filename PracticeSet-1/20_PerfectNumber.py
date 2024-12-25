'''Checking for Perfect Numbers
Difficulty: Easy
Topics: Basic Programming, Number Theory
Description: Write a program to determine if a number is a perfect number.
Example:
Input: number = 28
Output: Perfect Number
Explanation: 28 is a perfect number because its divisors (1, 2, 4, 7, 14) sum up to 28.'''

def perfectNumber(n):
    sum = 0
    for i in range (1, n):
        if n % i == 0:
            sum += i
    if n == sum:
        return 'Perfect NUmber'
    else:
        return 'Not Perfect Number'


print(perfectNumber(28))
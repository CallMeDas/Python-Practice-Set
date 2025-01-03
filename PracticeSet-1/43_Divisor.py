'''Finding All Divisors of a Number
Difficulty: Easy
Topics: Basic Programming, Mathematical Computations
Description: Write a program to find all divisors of a given number.
Example:
Input: number = 12
Output: 1, 2, 3, 4, 6, 12
Explanation: The divisors of 12 are 1, 2, 3, 4, 6, and 12.'''

def divisor (n):
    div = []
    for i in range (1, n + 1):
        if n % i == 0:
            div.append(i)
    return div


print(divisor(12))

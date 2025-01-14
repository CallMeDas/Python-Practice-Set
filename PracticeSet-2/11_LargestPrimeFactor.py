'''Finding the Largest Prime Factor of a Number
Difficulty: Medium
Topics: Number Theory
Description: Write a program to find the largest prime factor of a given number.
Example:
Input: number = 28
Output: 7
Explanation: The prime factors of 28 are 2 and 7, with the largest being 7.'''

def largestPrimeFactor(n):
    largest = -1

    while n % 2 == 0:
        largest = 2
        n //= 2
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest = factor
            n //= factor
        factor += 2
    if n > 2:
        largest = n

    return largest

print(largestPrimeFactor(28))
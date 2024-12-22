'''Checking for Prime Numbers
Difficulty: Easy
Topics: Basic Programming, Number Theory
Description: Write a program to determine if a number is prime.
Example:
Input: number = 7
Output: Prime
Explanation: 7 has no divisors other than 1 and itself, so it is a prime number.'''

def is_prime(n):
    if n < 2:
        return False
    for i in range (2, int(n ** 0.5) +1):
        if n % i == 0:
            return 'Not Prime'
    return 'Prime' 


print(is_prime(5))
'''Finding the Sum of Prime Factors of a Number
Difficulty: Medium
Topics: Number Theory, Mathematical Computations
Description: Write a program to find the sum of the prime factors of a given number.
Example:
Input: number = 12
Output: 5
Explanation: The prime factors of 12 are 2 and 3, and their sum is 2 + 3 = 5.'''

def sumPrimeFactors(n):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_factors = []
    for i in range(2, n + 1):
        if n % i == 0 and isPrime(i):
            prime_factors.append(i)

    return sum(prime_factors)


print(sumPrimeFactors(12))

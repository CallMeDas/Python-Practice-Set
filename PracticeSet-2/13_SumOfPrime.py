'''Finding the Sum of the First N Prime Numbers
Difficulty: Medium
Topics: Prime Numbers, Mathematical Computations
Description: Write a program to calculate the sum of the first N prime numbers.
Example:
Input: N = 4
Output: 17
Explanation: The sum of the first 4 prime numbers (2 + 3 + 5 + 7) is 17.'''


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(n):
    count = 0
    num = 2
    total_sum = 0

    while count < n:
        if is_prime(num):
            total_sum += num
            count += 1
        num += 1

    return total_sum

N = 4
print(f"The sum of the first {N} prime numbers is: {sum_of_primes(N)}")

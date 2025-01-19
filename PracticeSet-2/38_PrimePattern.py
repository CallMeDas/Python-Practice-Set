'''Generating a Pattern of Prime Numbers
Difficulty: Medium
Topics: Prime Numbers, Patterns
Description: Write a program to generate a pattern where each row contains the first few prime numbers.
Example:
Input: rows = 3
Output:

2  
3 5  
7 11 13  '''


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_pattern(rows):
    primes = []
    num = 2
    while len(primes) < (rows * (rows + 1)) // 2:
        if is_prime(num):
            primes.append(num)
        num += 1

    index = 0
    for i in range(1, rows + 1):
        for j in range(i):
            print(primes[index], end=" ")
            index += 1
        print()


rows = 3
generate_prime_pattern(rows)

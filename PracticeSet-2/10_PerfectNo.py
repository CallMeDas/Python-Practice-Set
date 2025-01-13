'''Finding the Number of Perfect Numbers Up to a Given Limit
Difficulty: Medium
Topics: Number Theory
Description: Write a program to find how many perfect numbers exist up to a given limit.
Example:
Input: limit = 30
Output: 1
Explanation: There is only one perfect number (6) up to 30.'''


def is_perfect_number(n):
    if n < 2:
        return False
    divisors_sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum == n

def count_perfect_numbers(limit):
    count = 0
    for num in range(2, limit + 1):
        if is_perfect_number(num):
            count += 1
    return count


limit = 30
print(f"Number of perfect numbers up to {limit}: {count_perfect_numbers(limit)}")

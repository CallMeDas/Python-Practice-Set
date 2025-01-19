'''Finding the Sum of the First N Even Numbers
Difficulty: Easy
Topics: Mathematical Computations
Description: Write a program to calculate the sum of the first N even numbers.
Example:
Input: N = 4
Output: 20
Explanation: The first 4 even numbers are 2, 4, 6, 8, and their sum is 20.
'''

def sum_of_even_numbers(n):
    return n * (n + 1)

N = 4
result = sum_of_even_numbers(N)
print(f"The sum of the first {N} even numbers is: {result}")

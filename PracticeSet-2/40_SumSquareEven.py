'''Finding the Sum of the Squares of All Even Numbers Up to N
Difficulty: Medium
Topics: Mathematical Computations
Description: Write a program to calculate the sum of squares of all even numbers up to a given N.
Example:
Input: N = 4
Output: 20
Explanation: The even numbers up to 4 are 2 and 4, and their squares are 4 and 16. The sum is 20.'''


def sum_of_squares_of_even_numbers(n):
    total = 0
    for i in range(2, n + 1, 2): 
        total += i ** 2
    return total


N = 4
result = sum_of_squares_of_even_numbers(N)
print(result)

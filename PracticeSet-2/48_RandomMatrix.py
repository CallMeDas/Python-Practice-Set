'''Generating a Square Matrix with Random Values
Difficulty: Easy
Topics: Random Number Generation, Matrix Operations
Description: Write a program to generate a square matrix where each element is a random value.
Example:
Input: size = 3
Output:

7 3 5  
2 6 9  
1 8 4  '''

import random

def generate_square_matrix(size):
    matrix = [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))


size = 3
matrix = generate_square_matrix(size)
print("Generated Matrix:")
print_matrix(matrix)

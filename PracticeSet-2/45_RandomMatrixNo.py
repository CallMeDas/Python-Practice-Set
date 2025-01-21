'''Generating a Matrix with Random Numbers
Difficulty: Easy
Topics: Random Number Generation, Matrix Operations
Description: Write a program to generate a matrix filled with random numbers.
Example:
Input: rows = 2, columns = 3
Output:

3 8 1  
7 4 6  '''

import random

def generate_random_matrix(rows, columns):
    matrix = []
    for _ in range(rows):
        row = [random.randint(1, 10) for _ in range(columns)]
        matrix.append(row)
    return matrix


rows = 2
columns = 3
matrix = generate_random_matrix(rows, columns)

for row in matrix:
    print(' '.join(map(str, row)))


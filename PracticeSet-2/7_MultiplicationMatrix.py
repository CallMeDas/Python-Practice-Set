'''Generating a Matrix with Multiplication Table
Difficulty: Easy
Topics: Arrays, Matrix Operations
Description: Write a program to generate a matrix where each element at position (i, j) is the product of i and j.
Example:
Input: size = 3
Output:

1 2 3  
2 4 6  
3 6 9  '''

def generateMultiplicationMatrix(size):
    matrix = []
    
    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            row.append(i * j)
        matrix.append(row)
    
    for row in matrix:
        print(' '.join(map(str, row)))

size = 3
generateMultiplicationMatrix(size)

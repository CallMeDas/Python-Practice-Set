'''Generating a Square Matrix of a Given Size
Difficulty: Medium
Topics: Arrays, Matrix Operations
Description: Write a program to generate a square matrix of a given size and fill it with sequential numbers.
Example:
Input: size = 3
Output:

1 2 3  
4 5 6  
7 8 9  
Explanation: A 3x3 matrix is generated with sequential numbers.'''

def SquareMatrix(size):
    matrix = []
    num = 1
    for i in range(size):
        row = []
        for j in range(size):
            row.append(num)
            num += 1
        matrix.append(row)
    return matrix

def printMatrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))



print(SquareMatrix(3))



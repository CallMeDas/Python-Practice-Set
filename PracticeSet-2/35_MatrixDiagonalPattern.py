'''Generating a Matrix with a Diagonal Pattern
Difficulty: Medium
Topics: Matrix Operations
Description: Write a program to create a matrix where elements form diagonal lines of a given pattern.
Example:
Input: size = 4
Output:

1 0 0 0  
1 1 0 0  
1 1 1 0  
1 1 1 1  '''


def generate_diagonal_pattern(size):
    matrix = [[0 for _ in range(size)] for _ in range(size)] 

    for i in range(size):
        for j in range(i + 1): 
            matrix[i][j] = 1

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

size = 4
matrix = generate_diagonal_pattern(size)
print_matrix(matrix)


'''Generating a Matrix with Alternating 0s and 1s
Difficulty: Easy
Topics: Arrays, Matrix Operations
Description: Write a program to generate a matrix where the elements alternate between 0 and 1.
Example:
Input: size = 3
Output:

0 1 0  
1 0 1  
0 1 0 '''

def generate_alternating_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append((i + j) % 2)
        matrix.append(row)
    return matrix

size = 3
result = generate_alternating_matrix(size)
for row in result:
    print(" ".join(map(str, row)))

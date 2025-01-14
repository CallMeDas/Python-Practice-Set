'''Generating a Matrix of Fibonacci Numbers
Difficulty: Medium
Topics: Arrays, Matrix Operations
Description: Write a program to generate a matrix where each element is a Fibonacci number.
Example:
Input: size = 3
Output:

1 1 2  
3 5 8  
13 21 34'''

def generate_fibonacci_matrix(size):
    fib_sequence = [0, 1]
    while len(fib_sequence) < (size * size + 1): 
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    matrix = []
    index = 1
    for i in range(size):
        row = []
        for j in range(size):
            row.append(fib_sequence[index])
            index += 1
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
        
size = 3
matrix = generate_fibonacci_matrix(size)
print_matrix(matrix)

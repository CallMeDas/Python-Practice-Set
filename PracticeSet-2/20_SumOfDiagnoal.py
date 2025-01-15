'''Finding the Sum of Diagonal Elements in a Matrix
Difficulty: Easy
Topics: Matrix Operations
Description: Write a program to calculate the sum of the diagonal elements in a square matrix.
Example:
Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: 15
Explanation: The sum of the diagonal elements (1 + 5 + 9) is 15.'''

def sum_of_diagonals(matrix):
    n = len(matrix) 
    diagonal_sum = 0

    for i in range(n):
        diagonal_sum += matrix[i][i]

    return diagonal_sum

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output = sum_of_diagonals(matrix)
print(output)


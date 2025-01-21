'''Finding the Largest Element in Each Row of a Matrix
Difficulty: Easy
Topics: Matrix Operations
Description: Write a program to find the largest element in each row of a matrix.
Example:
Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [3, 6, 9]
Explanation: The largest elements in each row are 3, 6, and 9.'''

def largest_in_each_row(matrix):
    return [max(row) for row in matrix]


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = largest_in_each_row(matrix)
print(result)

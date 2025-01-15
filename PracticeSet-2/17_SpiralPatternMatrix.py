'''Generating a Matrix with a Spiral Pattern
Difficulty: Medium
Topics: Arrays, Matrix Operations
Description: Write a program to generate a matrix filled with numbers in a spiral pattern.
Example:
Input: size = 3
Output:
1 2 3  
8 9 4  
7 6 5  '''


def generate_spiral_matrix(size):
    matrix = [[0] * size for _ in range(size)]
    num = 1
    top, bottom, left, right = 0, size - 1, 0, size - 1

    while top <= bottom and left <= right:

        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1


        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1


        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


size = 3
spiral_matrix = generate_spiral_matrix(size)
print_matrix(spiral_matrix)

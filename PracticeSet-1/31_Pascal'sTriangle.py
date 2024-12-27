'''Generating a Pascal’s Triangle
Difficulty: Medium
Topics: Arrays, Mathematical Computations
Description: Write a program to generate Pascal's Triangle up to a given number of rows.
Example:
Input: rows = 4
Output:

1  
1 1  
1 2 1  
1 3 3 1  
Explanation: Pascal's Triangle with 4 rows is generated.'''

def generatePascalsTriangle(rows):
    triangle = []

    for i in range(rows):
        row = [1] 
        if i > 0:  
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
        triangle.append(row)

    for row in triangle:
        print(" ".join(map(str, row)))


generatePascalsTriangle(4)


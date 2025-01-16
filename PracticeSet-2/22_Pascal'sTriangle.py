'''Generating Pascal’s Triangle Up to N Rows
Difficulty: Medium
Topics: Combinatorics
Description: Write a program to generate Pascal’s Triangle up to N rows.
Example:
Input: N = 3
Output:

1  
1 1  
1 2 1  '''

def generate_pascals_triangle(n):
    triangle = []
    
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)
        triangle.append(row)
    
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(2 * len(triangle[-1])))

N = 3
pascals_triangle = generate_pascals_triangle(N)
print_pascals_triangle(pascals_triangle)

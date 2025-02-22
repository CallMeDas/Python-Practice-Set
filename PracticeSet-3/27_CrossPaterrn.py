'''Print a Matrix with Cross Pattern of Numbers
Difficulty: Hard
Topics: Matrix Pattern
Hint: Print a matrix where the center forms a cross pattern with numbers.

Example 1: Input: n = 5
Output:

5   5
 4 4 
  3  
 4 4 
5   5
'''

def crossPattern(n):
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print(n - min(i, j, n - i - 1, n - j - 1), end="")
            else:
                print(" ", end="")
        print()

crossPattern(5)

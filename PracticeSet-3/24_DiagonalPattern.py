'''Print a Pattern with Diagonal Lines
Difficulty: Hard
Topics: Pattern Printing
Hint: Print a pattern with diagonal lines using characters. Each diagonal line should be aligned properly.

Example 1: Input: n = 4
Output:

A
B B
C   C
D     D
'''



def diagonalPattern(n):
    for i in range(n):
        for j in range(2 * i + 1):  
            if j == 0 or j == 2 * i:  
                print(chr(65 + i), end="")  
            else:
                print(" ", end="")
        print()  

diagonalPattern(4)

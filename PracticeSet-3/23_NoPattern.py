'''Print a Number Pyramid Pattern with Characters
Difficulty: Hard
Topics: Pattern Printing
Hint: Print a pyramid pattern using increasing characters, where each row increases in width and character range.

Example 1: Input: n = 3
Output:

  A
 BCD
EFGHI
'''


def charPyramid(n):
    ch = ord('A')
    for i in range(n):
        print(" " * (n - i - 1), end="")  
        for j in range(2 * i + 1): 
            print(chr(ch), end="")
            ch += 1  
        print() 

charPyramid(3)

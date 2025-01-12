'''Generating a Diamond Pattern of Stars
Difficulty: Medium
Topics: Patterns, Basic Programming
Description: Write a program to create a diamond pattern with stars of a given size.
Example:
Input: size = 5
Output:

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
  '''
def diamondPattern(size):
    for i in range(1, size + 1):
        print(' ' * (size - i) + '*' * (2 * i - 1))
    
    for i in range(size - 1, 0, -1):
        print(' ' * (size - i) + '*' * (2 * i - 1))

diamondPattern(5)


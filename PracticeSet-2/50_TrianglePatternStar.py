'''Generating a Triangle Pattern of Stars with a Given Height
Difficulty: Easy
Topics: Patterns
Description: Write a program to create a triangle pattern of stars with a specified height.
Example:
Input: height = 4
Output:

*  
**  
***  
****  '''


def patternStar(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print('*',end='')
        print()


print(patternStar(4))
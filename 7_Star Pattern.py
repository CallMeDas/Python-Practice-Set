'''Crafting Star Patterns
Difficulty: Easy
Topics: Basic Programming, Patterns
Description: Write a program to create different star patterns (e.g., pyramid, diamond).
Example:
Input: patternType = "pyramid", height = 5
Output:

    *
   ***
  *****
 *******
*********   '''


n=5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))
     

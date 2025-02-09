'''Print a Diamond Pattern with Numbers
Difficulty: Easy
Topics: Pattern Printing
Hint: Print a diamond pattern with numbers. The pattern should have a peak in the middle with symmetric rows above and below it.

Example 1: Input: n = 3
Output:

  1
 121
12321
 121
  1
  '''

def diamondNo(n):
    # Upper
    for i in range(1, n + 1):
        print(" " * (n - i), end="") 
        for j in range(1, i + 1): 
            print(j, end="") 
        for j in range(i - 1, 0, -1):  
            print(j, end="")  
        print()

    # Lower 
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")  
        for j in range(1, i + 1):  
            print(j, end="") 
        for j in range(i - 1, 0, -1):  
            print(j, end="")  
        print()


diamondNo(3)

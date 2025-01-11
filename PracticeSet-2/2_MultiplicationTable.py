'''Generating a Multiplication Table for a Range
Difficulty: Easy
Topics: Arrays, Basic Programming
Description: Write a program to generate multiplication tables for numbers within a specified range.
Example:
Input: start = 2, end = 4
Output:

2 x 1 = 2   3 x 1 = 3   4 x 1 = 4  
2 x 2 = 4   3 x 2 = 6   4 x 2 = 8  
2 x 3 = 6   3 x 3 = 9   4 x 3 = 12  
2 x 4 = 8   3 x 4 = 12  4 x 4 = 16 '''

def multiplicationTables(start, end):
    for i in range(1, 11):
        row = []
        for num in range(start, end + 1):
            row.append(f"{num} x {i} = {num * i}")
        print("   ".join(row))
    print()


multiplicationTables(2, 4)




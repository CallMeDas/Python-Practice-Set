'''Finding the Sum of Elements in an Array
Difficulty: Easy
Topics: Basic Programming, Arrays
Description: Write a program to find the sum of elements in an array.
Example:
Input: array = [1, 2, 3, 4, 5]
Output: 15
Explanation: The sum of the elements in the array is 15.'''

def sumOfArray(n):
    sum = 0
    for el in n:
        sum += el
    return f'Sum is {sum}'

print(sumOfArray([1, 2, 3, 4, 5]))
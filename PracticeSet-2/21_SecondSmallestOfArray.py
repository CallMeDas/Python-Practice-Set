'''Finding the Second Smallest Number in an Array
Difficulty: Easy
Topics: Arrays
Description: Write a program to find the second smallest number in an array.
Example:
Input: array = [12, 13, 1, 10, 34, 1]
Output: 10
Explanation: The second smallest number in the array is 10.'''

def second_smallest(arr):
    if len(arr) < 2:
        return "Array must contain at least two distinct elements."

    smallest = float('inf')
    second_smallest = float('inf')

    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif smallest < num < second_smallest:
            second_smallest = num

    return second_smallest if second_smallest != float('inf') else "No second smallest element exists."


array = [12, 13, 1, 10, 34, 1]
output = second_smallest(array)
print(output)

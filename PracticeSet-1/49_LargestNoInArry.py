'''Finding the Second Largest Number in an Array
Difficulty: Medium
Topics: Arrays, Sorting
Description: Write a program to find the second largest number in an array.
Example:
Input: array = [10, 20, 4, 45, 99]
Output: 45
Explanation: The second largest number in the array is 45.'''

def secondLargest(arr):
    if len(arr) < 2:
        return "Array must have at least two elements."
    
    largest = second = float('-inf')  
    
    for i in arr:
        if i > largest:
            second = largest
            largest = i      
        elif i > second and i != largest:
            second = i       

    return second if second != float('-inf') else "No second largest number exists."

# Example usage
print(secondLargest([10, 20, 4, 45, 99]))

    
'''Finding the Median of an Array
Difficulty: Medium
Topics: Arrays, Sorting
Description: Write a program to find the median of an array of numbers.
Example:
Input: array = [3, 1, 2, 4, 5]
Output: 3
Explanation: The median of the sorted array [1, 2, 3, 4, 5] is 3.'''

def findMedian(array):
    array.sort()
    n = len(array)
    if n % 2 == 1:
        return array[n // 2]
    else: 
        mid1, mid2 = array[n // 2 - 1], array[n // 2]
        return (mid1 + mid2) / 2


print(findMedian([3, 1, 2, 4, 5]))


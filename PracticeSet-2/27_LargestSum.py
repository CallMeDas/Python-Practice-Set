'''Finding the Largest Sum of a Subarray
Difficulty: Medium
Topics: Arrays, Dynamic Programming
Description: Write a program to find the largest sum of any contiguous subarray.
Example:
Input: array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The largest sum is 6, from the subarray [4, -1, 2, 1]'''

def max_subarray_sum(array):
    max_current = max_global = array[0]

    for num in array[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)

    return max_global


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(array)
print(result)

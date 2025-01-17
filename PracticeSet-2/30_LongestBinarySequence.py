'''Finding the Longest Sequence of Consecutive 1s in a Binary Array
Difficulty: Medium
Topics: Arrays, Binary Operations
Description: Write a program to find the longest sequence of consecutive 1s in a binary array.
Example:
Input: array = [1, 1, 0, 1, 1, 1]
Output: 3
Explanation: The longest sequence of 1s is [1, 1, 1] with length 3.'''


def longest_consecutive_ones(array):
    max_count = 0
    current_count = 0

    for num in array:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

array = [1, 1, 0, 1, 1, 1]
print(longest_consecutive_ones(array))

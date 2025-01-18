'''Finding the Median of a List of Numbers
Difficulty: Medium
Topics: Sorting, Mathematical Computations
Description: Write a program to find the median value of a list of numbers.
Example:
Input: list = [3, 1, 4, 1, 5]
Output: 3
Explanation: After sorting the list to [1, 1, 3, 4, 5], the median is 3.'''



def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2

    if n % 2 == 0:
        median = (numbers[mid - 1] + numbers[mid]) / 2
    else:
        median = numbers[mid]

    return median

numbers = [3, 1, 4, 1, 5]
result = find_median(numbers)
print(result)

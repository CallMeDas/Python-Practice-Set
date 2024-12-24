'''Sorting an Array
Difficulty: Easy
Topics: Basic Programming, Sorting Algorithms
Description: Write a program to sort an array of numbers in ascending order.
Example:
Input: array = [3, 1, 4, 1, 5, 9]
Output: [1, 1, 3, 4, 5, 9]
Explanation: The array sorted in ascending order is [1, 1, 3, 4, 5, 9].'''

def sortArray(n):
    for i in range(len(n)):
        min = i
        for j in range(i + 1, len(n)):
            if n[j] < n[min]:
                min = j
        n[i], n[min] = n[min], n[i]
    return n

print(sortArray([3, 1, 4, 1, 5, 9]))

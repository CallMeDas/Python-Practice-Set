
'''Finding the Mode of Numbers in an Array
Difficulty: Medium
Topics: Arrays, Statistical Analysis
Description: Write a program to find the mode (most frequent number) in an array.
Example:
Input: array = [1, 2, 2, 3, 4, 4, 4]
Output: 4
Explanation: The most frequent number in the array is 4.'''


def findMode(arr):
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1  
    

    max_freq = max(frequency.values())
    
    mode = [key for key, value in frequency.items() if value == max_freq]
    
  
    return mode if len(mode) > 1 else mode[0]


print(findMode([1, 2, 2, 3, 4, 4, 4]))  

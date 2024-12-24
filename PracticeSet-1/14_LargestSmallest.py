'''Finding the Largest and Smallest Numbers in an Array
Difficulty: Easy
Topics: Basic Programming, Arrays
Description: Write a program to find the largest and smallest numbers in an array.
Example:
Input: array = [4, 7, 1, 8, 5]
Output: Largest: 8, Smallest: 1
Explanation: The largest number in the array is 8 and the smallest is 1.'''

def largestSmallest(n):
    max = n[0]
    min = n[0]
    for i in n:
        if i > max:
            max = i
        if i < min:
            min = i
    
    return f'Largest : {max} \nSmallest : {min}'


print(largestSmallest([4, 7, 1, 8, 5,]))
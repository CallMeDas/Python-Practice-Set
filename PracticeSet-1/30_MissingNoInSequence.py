'''Finding Missing Numbers in a Sequence
Difficulty: Easy
Topics: Basic Programming, Arrays
Description: Write a program to find missing numbers in a sequence from 1 to n.
Example:
Input: sequence = [1, 2, 4, 5]
Output: [3]
Explanation: The missing number in the sequence from 1 to 5 is 3.'''

def missingNumber(n):
    miss_num = []
    for i in range (1, n[-1] + 1):
        if i not in n:
            miss_num.append(i)
            
    return miss_num



print(missingNumber([1, 2, 4, 5]))
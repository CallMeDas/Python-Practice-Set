'''Finding the Common Elements in Two Arrays
Difficulty: Medium
Topics: Arrays
Description: Write a program to find common elements between two arrays.
Example:
Input: array1 = [1, 2, 3, 4], array2 = [3, 4, 5, 6]
Output: [3, 4]
Explanation: The common elements between the two arrays are 3 and 4.'''

def find_common_elements(array1, array2):
    set1 = set(array1)
    set2 = set(array2)

    common_elements = list(set1 & set2)

    return sorted(common_elements)


array1 = [1, 2, 3, 4]
array2 = [3, 4, 5, 6]
result = find_common_elements(array1, array2)
print(result)

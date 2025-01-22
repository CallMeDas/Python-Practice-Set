'''Finding All Triplets in an Array That Sum to Zero
Difficulty: Medium
Topics: Arrays, Sorting
Description: Write a program to find all unique triplets in an array that sum to zero.
Example:
Input: array = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Explanation: The unique triplets that sum to zero are listed.'''


def three_sum(array):
    array.sort()
    triplets = []

    for i in range(len(array) - 2):
        if i > 0 and array[i] == array[i - 1]:
            continue

        left, right = i + 1, len(array) - 1

        while left < right:
            current_sum = array[i] + array[left] + array[right]

            if current_sum == 0:
                triplets.append([array[i], array[left], array[right]])
                
                while left < right and array[left] == array[left + 1]:
                    left += 1
                while left < right and array[right] == array[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return triplets


array = [-1, 0, 1, 2, -1, -4]
result = three_sum(array)
print(result)

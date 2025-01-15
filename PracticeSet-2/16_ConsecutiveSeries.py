'''Finding the Longest Consecutive Sequence in an Array
Difficulty: Medium
Topics: Arrays, Hashing
Description: Write a program to find the longest sequence of consecutive numbers in an array.
Example:
Input: array = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive sequence is [1, 2, 3, 4].'''


def longest_consecutive_sequence(array):
    if not array:
        return 0

    num_set = set(array)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


input_array = [100, 4, 200, 1, 3, 2]
result = longest_consecutive_sequence(input_array)
print(f"The longest consecutive sequence length is: {result}")

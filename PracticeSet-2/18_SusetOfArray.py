'''Finding All Subsets of a Set
Difficulty: Medium
Topics: Combinatorics
Description: Write a program to generate all possible subsets of a given set of numbers.
Example:
Input: set = [1, 2]
Output: [[], [1], [2], [1, 2]]
Explanation: The subsets of [1, 2] are the empty set, [1], [2], and [1, 2].'''





def find_subsets(input_set):
    subsets = [[]]  

    for num in input_set:
        subsets += [current + [num] for current in subsets]

    return subsets

input_set = [1, 2]
subsets = find_subsets(input_set)
print(subsets)

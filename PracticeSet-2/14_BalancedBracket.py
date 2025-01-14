'''Checking for a Balanced Bracket Sequence
Difficulty: Medium
Topics: String Manipulation, Stack
Description: Write a program to check if a given string with brackets is balanced.
Example:
Input: string = "{[()]}"
Output: True
Explanation: The brackets are balanced.'''


def is_balanced(string):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()

    return len(stack) == 0

input_string = "{[()]}"
print(f"The string '{input_string}' is balanced: {is_balanced(input_string)}")

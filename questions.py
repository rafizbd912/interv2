# Question 1
def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices
    of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
    You can return the answer in any order.
    Args:
    nums (List[int]): List of integers.
    target (int): Target sum.

    Returns:
    List[int]: Indices of the two numbers that add up to the target.
    """
    # YOUR CODE HERE
    num_map = {}

    for i, num in  enumerate(nums):
        difference = target - num
        if difference in num_map:
            return [num_map[difference], i]
        num_map[num]=i
    
    return []
            


# Question 2
def is_valid_parenthesis(s):
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    An input string is valid if:
    1. Open brackets are closed by the same type of brackets.
    2. Open brackets are closed in the correct order.

    Args:
    s (str): Input string.

    Returns:
    bool: True if the string is valid, False otherwise.
    """
    # YOUR CODE HERE

    stack = []
    mapping = {")":"(", "}":"{","]":"["}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char]!=top_element:
                return False
            else:
                stack.append(char)
    return not stack

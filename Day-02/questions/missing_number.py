"""
Problem: Missing Number
Difficulty: Easy

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in that range missing from the array.
"""


from pyparsing import nums


def missing_number(nums):
    """
    Time: O(?)
    Space: O(?)
    """
    for i in range(len(nums) + 1):
        if i not in nums:
             return i


if __name__ == "__main__":
    print(missing_number([3, 0, 1]))  # Expected: 2
    print(missing_number([0, 1]))     # Expected: 2

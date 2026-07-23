"""
Problem: Contains Duplicate
Difficulty: Easy

Given an integer array nums, return True if any value appears at least
twice in the array, and False if every element is distinct.
"""


def contains_duplicate(nums):
    """
    Time: O(n)
    Space: O(n)
    """
    unique_elements = set(nums)
    return len(unique_elements) < len(nums)


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))  # Expected: True
    print(contains_duplicate([1, 2, 3, 4]))  # Expected: False

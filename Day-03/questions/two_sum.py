"""
Problem: Two Sum
Difficulty: Easy

Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.
"""


def two_sum(nums, target):
    """
    Time: O(?)
    Space: O(?)
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # Expected: [0, 1]
    print(two_sum([3, 2, 4], 6))       # Expected: [1, 2]

"""
Problem: Range Sum Query - Immutable
Difficulty: Easy

Given nums, answer multiple sumRange(left, right) queries efficiently.
"""


class NumArray:
    def __init__(self, nums):
        # TODO: implement your solution here
        self.nums = nums

    def sum_range(self, left, right):
        """
        Time: O(?) per query
        """
        # TODO: implement your solution here
        pass


if __name__ == "__main__":
    arr = NumArray([-2, 0, 3, -5, 2, -1])
    print(arr.sum_range(0, 2))  # Expected: 1
    print(arr.sum_range(2, 5))  # Expected: -1

"""
Problem: Range Sum Query - Immutable
Difficulty: Easy
LeetCode: https://leetcode.com/problems/range-sum-query-immutable/

Given nums, answer multiple sumRange(left, right) queries efficiently.
"""

from typing import List


class NumArrayBruteforce:
    """
    Brute Force - Recompute the sum on every query.
    Build: O(1)
    Query: O(n)
    """

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sum_range(self, left: int, right: int) -> int:
        return sum(self.nums[left:right + 1])


class NumArrayOptimized:
    """
    Optimized - Precompute a prefix sum array once.
    Build: O(n)
    Query: O(1)

    Key Insight: prefix[i] holds the sum of the first i elements, so
    sumRange(left, right) == prefix[right+1] - prefix[left].
    """

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sum_range(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    arr = NumArrayOptimized(nums)

    test_cases = [((0, 2), 1), ((2, 5), -1), ((0, 5), -3)]

    for (left, right), expected in test_cases:
        result = arr.sum_range(left, right)
        status = "✅" if result == expected else "❌"
        print(f"{status} sumRange({left}, {right}) -> {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Build O(1), Query O(n)")
    print("Optimized:   Build O(n), Query O(1)")

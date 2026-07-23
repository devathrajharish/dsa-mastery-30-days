"""
Problem: Two Sum
Difficulty: Easy
LeetCode: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.
"""

from typing import List


def two_sum_bruteforce(nums: List[int], target: int) -> List[int]:
    """
    Brute Force - Check every pair.
    Time: O(n^2)
    Space: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_optimized(nums: List[int], target: int) -> List[int]:
    """
    Optimized - Hash map storing value -> index while scanning once.
    Time: O(n)
    Space: O(n)

    Key Insight: For each num, check if its complement (target - num)
    was already seen instead of searching the rest of the array.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]

    for nums, target, expected in test_cases:
        result = two_sum_optimized(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {nums}, target={target} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n^2), Space O(1)")
    print("Optimized:   Time O(n),   Space O(n)")

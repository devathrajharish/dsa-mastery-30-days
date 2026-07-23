"""
Problem: Contains Duplicate
Difficulty: Easy
LeetCode: https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return True if any value appears at least
twice in the array, and False if every element is distinct.
"""

from typing import List


def contains_duplicate_bruteforce(nums: List[int]) -> bool:
    """
    Brute Force - Compare every pair of elements.
    Time: O(n^2)
    Space: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate_optimized(nums: List[int]) -> bool:
    """
    Optimized - Track seen values in a hash set.
    Time: O(n) - single pass
    Space: O(n) - worst case store every element

    Key Insight: A set gives O(1) average membership checks,
    so we never need to re-scan the array.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def contains_duplicate_pythonic(nums: List[int]) -> bool:
    """
    One-liner using set size comparison.
    Time: O(n)
    Space: O(n)
    """
    return len(set(nums)) != len(nums)


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]

    for nums, expected in test_cases:
        result = contains_duplicate_optimized(nums)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {nums} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n^2), Space O(1)")
    print("Optimized:   Time O(n),  Space O(n)")

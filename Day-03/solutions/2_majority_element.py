"""
Problem: Majority Element
Difficulty: Easy
LeetCode: https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element (the one
that appears more than n / 2 times). Always exists.
"""

from collections import Counter
from typing import List


def majority_element_bruteforce(nums: List[int]) -> int:
    """
    Brute Force - Count every value with a hash map.
    Time: O(n)
    Space: O(n)
    """
    counts = Counter(nums)
    return max(counts, key=counts.get)


def majority_element_optimized(nums: List[int]) -> int:
    """
    Optimized - Boyer-Moore Voting Algorithm.
    Time: O(n)
    Space: O(1)

    Key Insight: Treat the majority value as +1 and everything else as
    -1 relative to it. The running "vote" can never fully cancel out
    because the majority element outnumbers all others combined.
    """
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
    ]

    for nums, expected in test_cases:
        result = majority_element_optimized(nums)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {nums} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n), Space O(n)")
    print("Optimized:   Time O(n), Space O(1)")

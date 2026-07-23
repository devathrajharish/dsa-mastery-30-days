"""
Problem: Missing Number
Difficulty: Easy
LeetCode: https://leetcode.com/problems/missing-number/

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in that range missing from the array.
"""

from typing import List


def missing_number_bruteforce(nums: List[int]) -> int:
    """
    Brute Force - Check membership of every expected value.
    Time: O(n^2) using `in` on a list (or O(n) with a set)
    Space: O(n)
    """
    n = len(nums)
    for i in range(n + 1):
        if i not in nums:
            return i
    return -1


def missing_number_optimized(nums: List[int]) -> int:
    """
    Optimized - Gauss sum formula: sum(0..n) - sum(nums).
    Time: O(n)
    Space: O(1)

    Key Insight: If nothing were missing, the array would sum to
    n*(n+1)/2. Whatever is missing is exactly that gap.
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


def missing_number_xor(nums: List[int]) -> int:
    """
    Alternative - XOR cancels out every matching pair.
    Time: O(n)
    Space: O(1)
    """
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result


if __name__ == "__main__":
    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ]

    for nums, expected in test_cases:
        result = missing_number_optimized(nums)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {nums} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n^2), Space O(n)")
    print("Optimized:   Time O(n),   Space O(1)")

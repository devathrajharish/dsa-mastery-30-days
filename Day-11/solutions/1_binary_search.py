"""
Problem: Binary Search
Difficulty: Easy
LeetCode: https://leetcode.com/problems/binary-search/

Given a sorted, distinct array nums and a target, return the index of
target, or -1 if it isn't present. Must run in O(log n).
"""

from typing import List


def binary_search_bruteforce(nums: List[int], target: int) -> int:
    """
    Brute Force - Linear scan (ignores the fact the array is sorted).
    Time: O(n)
    Space: O(1)
    """
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


def binary_search_optimized(nums: List[int], target: int) -> int:
    """
    Optimized - Classic binary search.
    Time: O(log n)
    Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ]

    for nums, target, expected in test_cases:
        result = binary_search_optimized(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {nums}, target={target} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n),     Space O(1)")
    print("Optimized:   Time O(log n), Space O(1)")

"""
Problem: Find Minimum in Rotated Sorted Array
Difficulty: Medium
LeetCode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Given a rotated ascending array of unique values, find the minimum
element in O(log n).
"""

from typing import List


def find_min_bruteforce(nums: List[int]) -> int:
    """
    Brute Force - Linear scan.
    Time: O(n)
    Space: O(1)
    """
    return min(nums)


def find_min_optimized(nums: List[int]) -> int:
    """
    Optimized - Binary search comparing mid to right boundary.
    Time: O(log n)
    Space: O(1)

    Key Insight: If nums[mid] > nums[right], the minimum must be to the
    right of mid (rotation point is there). Otherwise, the minimum is
    at mid or to its left.
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


if __name__ == "__main__":
    test_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
    ]

    for nums, expected in test_cases:
        result = find_min_optimized(nums)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {nums} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n),     Space O(1)")
    print("Optimized:   Time O(log n), Space O(1)")

"""
Problem: Search in Rotated Sorted Array
Difficulty: Medium
LeetCode: https://leetcode.com/problems/search-in-rotated-sorted-array/

Search for target in a rotated ascending array of distinct values.
Must run in O(log n).
"""

from typing import List


def search_bruteforce(nums: List[int], target: int) -> int:
    """
    Brute Force - Linear scan (ignores rotation structure).
    Time: O(n)
    Space: O(1)
    """
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


def search_optimized(nums: List[int], target: int) -> int:
    """
    Optimized - Modified binary search.
    Time: O(log n)
    Space: O(1)

    Key Insight: At least one half of [left, right] is always properly
    sorted. Check if target lies in that half's range to decide which
    side to keep.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:  # left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ]

    for nums, target, expected in test_cases:
        result = search_optimized(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {nums}, target={target} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n),     Space O(1)")
    print("Optimized:   Time O(log n), Space O(1)")

"""
Problem: Search Insert Position
Difficulty: Easy
LeetCode: https://leetcode.com/problems/search-insert-position/

Given a sorted, distinct array nums and a target, return its index if
found, else the index where it would be inserted. Must run O(log n).
"""

from typing import List


def search_insert_bruteforce(nums: List[int], target: int) -> int:
    """
    Brute Force - Linear scan for the first element >= target.
    Time: O(n)
    Space: O(1)
    """
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)


def search_insert_optimized(nums: List[int], target: int) -> int:
    """
    Optimized - Binary search; when no exact match is found, `left`
    naturally lands on the correct insertion index.
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

    return left


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
    ]

    for nums, target, expected in test_cases:
        result = search_insert_optimized(nums, target)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {nums}, target={target} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n),     Space O(1)")
    print("Optimized:   Time O(log n), Space O(1)")

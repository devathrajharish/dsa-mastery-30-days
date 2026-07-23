"""
Problem: Remove Duplicates from Sorted Array
Difficulty: Easy
LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove duplicates in-place so each unique
element appears once; return k, the count of unique elements.
"""

from typing import List


def remove_duplicates_bruteforce(nums: List[int]) -> int:
    """
    Brute Force - Collect unique values (order preserved since sorted),
    then copy back into nums.
    Time: O(n)
    Space: O(n) - extra list
    """
    unique = []
    for num in nums:
        if not unique or unique[-1] != num:
            unique.append(num)
    nums[:len(unique)] = unique
    return len(unique)


def remove_duplicates_optimized(nums: List[int]) -> int:
    """
    Optimized - Two-pointer in-place overwrite.
    Time: O(n)
    Space: O(1)

    Key Insight: Because nums is sorted, duplicates are always adjacent.
    `left` marks the last confirmed-unique slot; `right` scans forward
    looking for the next different value.
    """
    if not nums:
        return 0

    left = 0
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]

    return left + 1


if __name__ == "__main__":
    test_cases = [
        ([1, 1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5),
    ]

    for nums, expected in test_cases:
        working = nums.copy()
        result = remove_duplicates_optimized(working)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {nums} -> k={result} (Expected: {expected}), nums={working[:result]}")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n), Space O(n)")
    print("Optimized:   Time O(n), Space O(1)")

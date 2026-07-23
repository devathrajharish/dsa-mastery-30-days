"""
Problem: Move Zeroes
Difficulty: Easy
LeetCode: https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end while maintaining
the relative order of the non-zero elements, in-place.
"""

from typing import List


def move_zeroes_bruteforce(nums: List[int]) -> None:
    """
    Brute Force - Build a new list of non-zeros, pad with zeros, copy back.
    Time: O(n)
    Space: O(n) - extra list
    """
    non_zeros = [num for num in nums if num != 0]
    non_zeros += [0] * (len(nums) - len(non_zeros))
    nums[:] = non_zeros


def move_zeroes_optimized(nums: List[int]) -> None:
    """
    Optimized - Two-pointer in-place swap.
    Time: O(n)
    Space: O(1)

    Key Insight: `left` tracks the next slot for a non-zero value.
    Every time `right` finds a non-zero, swap it into place.
    """
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1


if __name__ == "__main__":
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
    ]

    for nums, expected in test_cases:
        working = nums.copy()
        move_zeroes_optimized(working)
        status = "✅" if working == expected else "❌"
        print(f"{status} Input: {nums} -> Output: {working} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n), Space O(n)")
    print("Optimized:   Time O(n), Space O(1)")

"""
Problem: Running Sum of 1D Array
Difficulty: Easy
LeetCode: https://leetcode.com/problems/running-sum-of-1d-array/

Given an array nums, return an array runningSum where
runningSum[i] is the sum of all elements nums[0]...nums[i].
"""

from typing import List


def running_sum_bruteforce(nums: List[int]) -> List[int]:
    """
    Brute Force Approach - Calculate sum from beginning each time
    Time: O(n²) - For each element, recalculate sum
    Space: O(1) - Only output array
    """
    result = []
    for i in range(len(nums)):
        current_sum = sum(nums[:i+1])
        result.append(current_sum)
    return result


def running_sum_optimized(nums: List[int]) -> List[int]:
    """
    Optimized Approach - Keep running total
    Time: O(n) - Single pass through array
    Space: O(1) - Only output array

    Key Insight: Don't recalculate sum each time.
    Just add current element to previous sum!
    """
    result = []
    current_sum = 0

    for num in nums:
        current_sum += num
        result.append(current_sum)

    return result


def running_sum_inplace(nums: List[int]) -> List[int]:
    """
    In-place Variation - Modify input array directly
    Time: O(n)
    Space: O(1) if we don't count output array
    """
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
        ([1], [1]),
        ([-1, 1, 2], [-1, 0, 2]),
    ]

    for nums, expected in test_cases:
        result = running_sum_optimized(nums.copy())
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {nums} -> Output: {result} (Expected: {expected})")

    # Complexity Analysis
    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n²), Space O(1)")
    print("Optimized:   Time O(n),  Space O(1)")
    print("In-place:    Time O(n),  Space O(1)")

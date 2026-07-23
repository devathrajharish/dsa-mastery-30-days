"""
Problem: Maximum Average Subarray I
Difficulty: Easy
LeetCode: https://leetcode.com/problems/maximum-average-subarray-i/

Given nums and k, find the contiguous subarray of length k with the
maximum average and return that average.
"""

from typing import List


def find_max_average_bruteforce(nums: List[int], k: int) -> float:
    """
    Brute Force - Recompute the sum of each window from scratch.
    Time: O(n*k)
    Space: O(1)
    """
    n = len(nums)
    best_sum = sum(nums[:k])
    for start in range(1, n - k + 1):
        best_sum = max(best_sum, sum(nums[start:start + k]))
    return best_sum / k


def find_max_average_optimized(nums: List[int], k: int) -> float:
    """
    Optimized - Sliding window sum.
    Time: O(n)
    Space: O(1)

    Key Insight: Moving the window by one only changes two elements -
    add the new right element, remove the element that fell out.
    """
    window_sum = sum(nums[:k])
    best_sum = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        best_sum = max(best_sum, window_sum)

    return best_sum / k


if __name__ == "__main__":
    test_cases = [
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5.0),
    ]

    for nums, k, expected in test_cases:
        result = find_max_average_optimized(nums, k)
        status = "✅" if abs(result - expected) < 1e-5 else "❌"
        print(f"{status} Input: {nums}, k={k} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n*k), Space O(1)")
    print("Optimized:   Time O(n),   Space O(1)")

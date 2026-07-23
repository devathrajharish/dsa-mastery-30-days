"""
Problem: Maximum Sum Subarray of Size K
Difficulty: Easy

Given a positive-integer array nums and integer k, find the maximum
sum of any contiguous subarray of size exactly k.
"""

from typing import List


def max_sum_subarray_bruteforce(nums: List[int], k: int) -> int:
    """
    Brute Force - Recompute the sum of each window from scratch.
    Time: O(n*k)
    Space: O(1)
    """
    n = len(nums)
    best = sum(nums[:k])
    for start in range(1, n - k + 1):
        best = max(best, sum(nums[start:start + k]))
    return best


def max_sum_subarray_optimized(nums: List[int], k: int) -> int:
    """
    Optimized - Sliding window sum.
    Time: O(n)
    Space: O(1)
    """
    window_sum = sum(nums[:k])
    best = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        best = max(best, window_sum)

    return best


if __name__ == "__main__":
    test_cases = [
        ([2, 1, 5, 1, 3, 2], 3, 9),
        ([2, 3, 4, 1, 5], 2, 7),
    ]

    for nums, k, expected in test_cases:
        result = max_sum_subarray_optimized(nums, k)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {nums}, k={k} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n*k), Space O(1)")
    print("Optimized:   Time O(n),   Space O(1)")

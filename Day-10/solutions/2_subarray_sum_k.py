"""
Problem: Subarray Sum Equals K
Difficulty: Medium
LeetCode: https://leetcode.com/problems/subarray-sum-equals-k/

Given nums and k, return the number of contiguous subarrays whose sum
equals k.
"""

from collections import defaultdict
from typing import List


def subarray_sum_bruteforce(nums: List[int], k: int) -> int:
    """
    Brute Force - Sum every contiguous subarray.
    Time: O(n^2)
    Space: O(1)
    """
    n = len(nums)
    count = 0

    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += nums[end]
            if current_sum == k:
                count += 1

    return count


def subarray_sum_optimized(nums: List[int], k: int) -> int:
    """
    Optimized - Running prefix sum with a hash map of how many times
    each prefix sum has occurred.
    Time: O(n)
    Space: O(n)

    Key Insight: A subarray (i, j] sums to k exactly when
    prefix[j] - prefix[i] == k, i.e. prefix[i] == prefix[j] - k.
    Count how many earlier prefixes equal (current prefix - k).
    """
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1  # empty prefix, handles subarrays starting at index 0

    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num
        count += prefix_counts[current_sum - k]
        prefix_counts[current_sum] += 1

    return count


if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
    ]

    for nums, k, expected in test_cases:
        result = subarray_sum_optimized(nums, k)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {nums}, k={k} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n^2), Space O(1)")
    print("Optimized:   Time O(n),   Space O(n)")

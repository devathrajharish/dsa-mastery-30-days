"""
Problem: Next Greater Element I
Difficulty: Easy
LeetCode: https://leetcode.com/problems/next-greater-element-i/

For each element of nums1, find its next greater element in nums2 (or
-1 if none exists).
"""

from typing import List


def next_greater_element_bruteforce(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Brute Force - For each nums1 value, scan forward in nums2.
    Time: O(n * m)
    Space: O(1) extra (excluding output)
    """
    result = []
    for target in nums1:
        idx = nums2.index(target)
        answer = -1
        for j in range(idx + 1, len(nums2)):
            if nums2[j] > target:
                answer = nums2[j]
                break
        result.append(answer)
    return result


def next_greater_element_optimized(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Optimized - Monotonic decreasing stack precomputes next-greater for
    every value in nums2 in one pass.
    Time: O(n + m)
    Space: O(m)
    """
    next_greater = {}
    stack = []

    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)

    return [next_greater.get(num, -1) for num in nums1]


if __name__ == "__main__":
    test_cases = [
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
    ]

    for nums1, nums2, expected in test_cases:
        result = next_greater_element_optimized(nums1, nums2)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: nums1={nums1}, nums2={nums2} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n*m), Space O(1)")
    print("Optimized:   Time O(n+m), Space O(m)")

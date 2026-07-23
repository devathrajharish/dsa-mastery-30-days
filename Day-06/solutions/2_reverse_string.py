"""
Problem: Reverse String
Difficulty: Easy
LeetCode: https://leetcode.com/problems/reverse-string/

Reverse an array of characters in-place, O(1) extra space.
"""

from typing import List


def reverse_string_bruteforce(s: List[str]) -> None:
    """
    Brute Force - Build a reversed copy, then copy back.
    Time: O(n)
    Space: O(n)
    """
    s[:] = s[::-1]


def reverse_string_optimized(s: List[str]) -> None:
    """
    Optimized - Two-pointer in-place swap.
    Time: O(n)
    Space: O(1)
    """
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    test_cases = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ]

    for s, expected in test_cases:
        working = s.copy()
        reverse_string_optimized(working)
        status = "✅" if working == expected else "❌"
        print(f"{status} Input: {s} -> Output: {working} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n), Space O(n)")
    print("Optimized:   Time O(n), Space O(1)")

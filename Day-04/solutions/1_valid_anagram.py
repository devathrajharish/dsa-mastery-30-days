"""
Problem: Valid Anagram
Difficulty: Easy
LeetCode: https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return True if t is an anagram of s.
"""

from collections import Counter


def is_anagram_bruteforce(s: str, t: str) -> bool:
    """
    Brute Force - Sort both strings and compare.
    Time: O(n log n)
    Space: O(n)
    """
    return sorted(s) == sorted(t)


def is_anagram_optimized(s: str, t: str) -> bool:
    """
    Optimized - Compare character frequency counts.
    Time: O(n)
    Space: O(1) - at most 26 lowercase letters

    Key Insight: Two strings are anagrams exactly when every character
    appears the same number of times in both.
    """
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
    ]

    for s, t, expected in test_cases:
        result = is_anagram_optimized(s, t)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: s={s!r}, t={t!r} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n log n), Space O(n)")
    print("Optimized:   Time O(n),       Space O(1)")

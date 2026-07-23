"""
Problem: Longest Substring Without Repeating Characters
Difficulty: Medium
LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without
repeating characters.
"""


def length_of_longest_substring_bruteforce(s: str) -> int:
    """
    Brute Force - Check every substring for duplicate characters.
    Time: O(n^2)
    Space: O(min(n, charset))
    """
    n = len(s)
    best = 0

    for start in range(n):
        seen = set()
        for end in range(start, n):
            if s[end] in seen:
                break
            seen.add(s[end])
            best = max(best, end - start + 1)

    return best


def length_of_longest_substring_optimized(s: str) -> int:
    """
    Optimized - Sliding window with a dict mapping char -> last seen index.
    Time: O(n)
    Space: O(min(n, charset))

    Key Insight: When a repeat is found, jump `left` directly past the
    previous occurrence instead of shrinking one character at a time.
    """
    last_seen = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
    ]

    for s, expected in test_cases:
        result = length_of_longest_substring_optimized(s)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {s!r} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n^2), Space O(min(n,charset))")
    print("Optimized:   Time O(n),   Space O(min(n,charset))")

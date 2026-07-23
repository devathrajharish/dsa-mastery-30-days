"""
Problem: Longest Repeating Character Replacement
Difficulty: Medium
LeetCode: https://leetcode.com/problems/longest-repeating-character-replacement/

Given s (uppercase letters) and integer k, you may replace up to k
characters; return the length of the longest run of one repeated
letter achievable.
"""

from collections import Counter


def character_replacement_bruteforce(s: str, k: int) -> int:
    """
    Brute Force - Check every substring; it's valid if
    (length - most common letter's count) <= k.
    Time: O(n^2)
    Space: O(26) per substring
    """
    n = len(s)
    best = 0

    for start in range(n):
        counts = Counter()
        for end in range(start, n):
            counts[s[end]] += 1
            window_len = end - start + 1
            if window_len - max(counts.values()) <= k:
                best = max(best, window_len)

    return best


def character_replacement_optimized(s: str, k: int) -> int:
    """
    Optimized - Sliding window tracking the count of the most frequent
    letter seen so far in the window.
    Time: O(n)
    Space: O(26)

    Key Insight: A window of length L is valid if L - max_freq <= k.
    max_freq never needs to decrease when shrinking - it can only be
    stale (too high), which never causes a false "valid" result, so we
    never need to recompute it exactly.
    """
    counts = Counter()
    left = 0
    max_freq = 0
    best = 0

    for right, ch in enumerate(s):
        counts[ch] += 1
        max_freq = max(max_freq, counts[ch])

        window_len = right - left + 1
        if window_len - max_freq > k:
            counts[s[left]] -= 1
            left += 1
        else:
            best = max(best, window_len)

    return best


if __name__ == "__main__":
    test_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
    ]

    for s, k, expected in test_cases:
        result = character_replacement_optimized(s, k)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: s={s!r}, k={k} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n^2), Space O(26)")
    print("Optimized:   Time O(n),   Space O(26)")

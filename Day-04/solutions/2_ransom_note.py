"""
Problem: Ransom Note
Difficulty: Easy
LeetCode: https://leetcode.com/problems/ransom-note/

Given ransomNote and magazine, return True if ransomNote can be built
using magazine's letters (each letter usable only once).
"""

from collections import Counter


def can_construct_bruteforce(ransom_note: str, magazine: str) -> bool:
    """
    Brute Force - Remove each needed letter from a mutable list copy.
    Time: O(n * m) - list.remove is O(m)
    Space: O(m)
    """
    available = list(magazine)
    for ch in ransom_note:
        if ch in available:
            available.remove(ch)
        else:
            return False
    return True


def can_construct_optimized(ransom_note: str, magazine: str) -> bool:
    """
    Optimized - Compare frequency counts.
    Time: O(n + m)
    Space: O(1) - at most 26 lowercase letters

    Key Insight: ransomNote can be built from magazine exactly when
    magazine has at least as many of each letter as ransomNote needs.
    """
    note_counts = Counter(ransom_note)
    magazine_counts = Counter(magazine)

    for ch, needed in note_counts.items():
        if magazine_counts[ch] < needed:
            return False
    return True


if __name__ == "__main__":
    test_cases = [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
    ]

    for note, magazine, expected in test_cases:
        result = can_construct_optimized(note, magazine)
        status = "✅" if result == expected else "❌"
        print(f"{status} ransomNote={note!r}, magazine={magazine!r} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n*m), Space O(m)")
    print("Optimized:   Time O(n+m), Space O(1)")

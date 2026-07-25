"""
Problem: Valid Anagram
Difficulty: Easy

Given two strings s and t, return True if t is an anagram of s.
"""


def is_anagram(s, t):
    """
    Time: O(?)
    Space: O(?)
    """
    if len(s) != len(t):
        return False
    s_count = {}
    for char in s:
        if char in s_count:
            s_count[char] += 1
        else:
            s_count[char] = 1
    for char in t:
        if char in s_count:
            s_count[char] -= 1
        else:
            return False
    for char in s_count:
        if s_count[char] != 0:
            return False
    return True

if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))  # Expected: True
    print(is_anagram("rat", "car"))          # Expected: False

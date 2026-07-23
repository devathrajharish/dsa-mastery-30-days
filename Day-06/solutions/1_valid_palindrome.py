"""
Problem: Valid Palindrome
Difficulty: Easy
LeetCode: https://leetcode.com/problems/valid-palindrome/

Given a string s, return True if it's a palindrome considering only
alphanumeric characters and ignoring case.
"""


def is_palindrome_bruteforce(s: str) -> bool:
    """
    Brute Force - Build a cleaned string, compare to its reverse.
    Time: O(n)
    Space: O(n) - cleaned string copy
    """
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    return cleaned == cleaned[::-1]


def is_palindrome_optimized(s: str) -> bool:
    """
    Optimized - Two pointers from both ends, skipping non-alphanumeric chars.
    Time: O(n)
    Space: O(1)

    Key Insight: We never need to build a cleaned copy - just skip
    irrelevant characters as the pointers move inward.
    """
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
    ]

    for s, expected in test_cases:
        result = is_palindrome_optimized(s)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {s!r} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n), Space O(n)")
    print("Optimized:   Time O(n), Space O(1)")

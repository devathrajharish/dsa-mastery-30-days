"""
Problem: Valid Parentheses
Difficulty: Easy
LeetCode: https://leetcode.com/problems/valid-parentheses/

Given a string of bracket characters, determine if it is valid
(every bracket is closed in the correct order).
"""


def is_valid_bruteforce(s: str) -> bool:
    """
    Brute Force - Repeatedly remove any matched adjacent pair until the
    string stops changing.
    Time: O(n^2)
    Space: O(n)
    """
    pairs = ("()", "[]", "{}")
    changed = True
    while changed:
        changed = False
        for pair in pairs:
            if pair in s:
                s = s.replace(pair, "", 1)
                changed = True
    return s == ""


def is_valid_optimized(s: str) -> bool:
    """
    Optimized - Stack matching each closing bracket to the most recent
    open bracket.
    Time: O(n)
    Space: O(n)
    """
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)

    return not stack


if __name__ == "__main__":
    test_cases = [
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
    ]

    for s, expected in test_cases:
        result = is_valid_optimized(s)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {s!r} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n^2), Space O(n)")
    print("Optimized:   Time O(n),   Space O(n)")

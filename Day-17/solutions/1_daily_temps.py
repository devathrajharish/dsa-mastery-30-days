"""
Problem: Daily Temperatures
Difficulty: Medium
LeetCode: https://leetcode.com/problems/daily-temperatures/

Return, for each day, how many days until a warmer temperature (0 if
none exists).
"""

from typing import List


def daily_temperatures_bruteforce(temperatures: List[int]) -> List[int]:
    """
    Brute Force - For each day, scan forward for a warmer day.
    Time: O(n^2)
    Space: O(1) extra (excluding output)
    """
    n = len(temperatures)
    answer = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                answer[i] = j - i
                break

    return answer


def daily_temperatures_optimized(temperatures: List[int]) -> List[int]:
    """
    Optimized - Monotonic decreasing stack of indices awaiting a
    warmer day.
    Time: O(n) - each index pushed and popped at most once
    Space: O(n)
    """
    n = len(temperatures)
    answer = [0] * n
    stack = []  # indices with temperatures waiting for a warmer day

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        stack.append(i)

    return answer


if __name__ == "__main__":
    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ]

    for temps, expected in test_cases:
        result = daily_temperatures_optimized(temps)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {temps} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n^2), Space O(1)")
    print("Optimized:   Time O(n),   Space O(n)")

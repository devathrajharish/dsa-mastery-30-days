"""
Problem: Min Stack
Difficulty: Medium
LeetCode: https://leetcode.com/problems/min-stack/

Design a stack supporting push/pop/top/getMin, all O(1).
"""


class MinStackBruteforce:
    """
    Brute Force - getMin() scans the entire stack.
    push/pop/top: O(1)
    getMin: O(n)
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return min(self.stack)


class MinStackOptimized:
    """
    Optimized - A parallel stack tracks the minimum seen so far at each
    level, so getMin never needs to scan.
    push/pop/top/getMin: all O(1)

    Key Insight: Push the current minimum alongside every value, so
    popping automatically "restores" the previous minimum too.
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = min(val, self.min_stack[-1]) if self.min_stack else val
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    ms = MinStackOptimized()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)

    test_cases = [
        ("getMin", -3),
    ]
    for _, expected in test_cases:
        result = ms.get_min()
        status = "✅" if result == expected else "❌"
        print(f"{status} getMin() -> {result} (Expected: {expected})")

    ms.pop()
    result = ms.top()
    status = "✅" if result == 0 else "❌"
    print(f"{status} top() -> {result} (Expected: 0)")

    result = ms.get_min()
    status = "✅" if result == -2 else "❌"
    print(f"{status} getMin() -> {result} (Expected: -2)")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: push/pop/top O(1), getMin O(n)")
    print("Optimized:   push/pop/top/getMin all O(1)")

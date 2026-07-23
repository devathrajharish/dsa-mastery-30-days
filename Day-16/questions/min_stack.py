"""
Problem: Min Stack
Difficulty: Medium

Design a stack supporting push/pop/top/getMin, all O(1).
"""


class MinStack:
    def __init__(self):
        # TODO: implement your solution here
        self.stack = []

    def push(self, val):
        pass

    def pop(self):
        pass

    def top(self):
        pass

    def get_min(self):
        pass


if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.get_min())  # Expected: -3

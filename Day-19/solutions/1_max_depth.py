"""
Problem: Maximum Depth of Binary Tree
Difficulty: Easy
LeetCode: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """Helper: build a binary tree from a LeetCode-style level-order
    list (None marks a missing child)."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def max_depth_iterative(root):
    """
    Iterative - BFS, counting how many levels are processed.
    Time: O(n)
    Space: O(n) - queue can hold a full level
    """
    if not root:
        return 0

    depth = 0
    queue = deque([root])

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth


def max_depth_recursive(root):
    """
    Optimized/cleanest - Recursive DFS.
    Time: O(n)
    Space: O(h) - recursion call stack, h = tree height
    """
    if not root:
        return 0

    return 1 + max(max_depth_recursive(root.left), max_depth_recursive(root.right))


if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
    ]

    for values, expected in test_cases:
        root = build_tree(values)
        result = max_depth_recursive(root)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {values} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Iterative (BFS): Time O(n), Space O(n)")
    print("Recursive (DFS): Time O(n), Space O(h)")

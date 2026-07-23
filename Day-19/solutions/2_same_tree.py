"""
Problem: Same Tree
Difficulty: Easy
LeetCode: https://leetcode.com/problems/same-tree/

Given roots of two binary trees, check if they are structurally
identical with the same node values.
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


def is_same_tree_iterative(p, q):
    """
    Iterative - BFS comparing both trees node-by-node in lockstep.
    Time: O(n)
    Space: O(n)
    """
    queue = deque([(p, q)])

    while queue:
        node_p, node_q = queue.popleft()

        if not node_p and not node_q:
            continue
        if not node_p or not node_q or node_p.val != node_q.val:
            return False

        queue.append((node_p.left, node_q.left))
        queue.append((node_p.right, node_q.right))

    return True


def is_same_tree_recursive(p, q):
    """
    Optimized/cleanest - Recursive DFS.
    Time: O(n)
    Space: O(h) - recursion call stack
    """
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False

    return is_same_tree_recursive(p.left, q.left) and is_same_tree_recursive(p.right, q.right)


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
    ]

    for p_vals, q_vals, expected in test_cases:
        p = build_tree(p_vals)
        q = build_tree(q_vals)
        result = is_same_tree_recursive(p, q)
        status = "✅" if result == expected else "❌"
        print(f"{status} p={p_vals}, q={q_vals} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Iterative (BFS): Time O(n), Space O(n)")
    print("Recursive (DFS): Time O(n), Space O(h)")

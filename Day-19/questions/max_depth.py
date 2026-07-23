"""
Problem: Maximum Depth of Binary Tree
Difficulty: Easy

Given the root of a binary tree, return its maximum depth.
"""

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


def max_depth(root):
    """
    Time: O(?)
    Space: O(?)
    """
    # TODO: implement your solution here
    pass


if __name__ == "__main__":
    root = build_tree([3, 9, 20, None, None, 15, 7])
    print(max_depth(root))  # Expected: 3

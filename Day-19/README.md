# Day 19: Trees and DFS

## 🎯 Learning Objectives

- Understand Recursive traversal
- Understand Base cases
- Understand Subtree processing

---

## 📚 Concept: Trees and DFS

### Key Ideas

- Recursive traversal
- Base cases
- Subtree processing

### Real-World Applications

- Computing folder/file sizes recursively in a file system tree
- Comparing two versions of a UI component tree for equality (diffing)

---

## 💡 Core Pattern

### Template

```python
def dfs(node):
    if not node:
        return

    dfs(node.left)
    dfs(node.right)
```

### Pattern Recognition Clue
Fully explore branches or recursively process subtrees.

---

## 🧠 Key Insights

1. `if not node: return` is the base case almost every tree recursion needs — it's what stops the recursion at leaves without a null-pointer error.
2. Depth and equality problems are both 'combine the answer from left and right subtrees' — depth uses `max`, equality uses `and`.
3. DFS naturally uses the call stack as its 'memory', which is why space complexity is O(h) (tree height), not O(n), for many tree problems.

---

## 📋 Practice Problems

### Problem 1: Maximum Depth of Binary Tree
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/maximum-depth-of-binary-tree/

**Problem Statement:**
Given the `root` of a binary tree, return its maximum depth — the number of nodes along the longest path from the root node down to the farthest leaf node.

**Examples:**
```
Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2
```

**Constraints:**
- Number of nodes in [0, 10^4]
- -100 <= Node.val <= 100

**Solution Location:** [solutions/1_max_depth.py](solutions/1_max_depth.py)
**Practice Location:** [questions/max_depth.py](questions/max_depth.py)

**Approaches to Consider:**
- Iterative: BFS level-by-level counting levels, O(n)
- Optimized/cleanest: recursive DFS, O(n) time / O(h) space
- Edge case: empty tree

### Problem 2: Same Tree
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/same-tree/

**Problem Statement:**
Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Examples:**
```
Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false
```

**Constraints:**
- Number of nodes in each tree in [0, 100]
- -10^4 <= Node.val <= 10^4

**Solution Location:** [solutions/2_same_tree.py](solutions/2_same_tree.py)
**Practice Location:** [questions/same_tree.py](questions/same_tree.py)

**Approaches to Consider:**
- Iterative: BFS comparing two queues in lockstep, O(n)
- Optimized/cleanest: recursive DFS comparing values and subtrees, O(n)
- Edge case: both trees empty

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Maximum Depth of Binary Tree)
- [ ] Solve Problem 2 (Same Tree)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- Every recursive tree function needs a base case for the null/leaf node.
- Most tree problems are 'solve for left, solve for right, combine' — identify what the combine step is (max, sum, and, etc.).
- Recursive DFS space cost is proportional to tree height, not size — this matters for very unbalanced trees.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 20](../Day-20/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

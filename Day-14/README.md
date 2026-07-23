# Day 14: Fast & Slow Pointers

## 🎯 Learning Objectives

- Understand Floyd's algorithm
- Understand Cycle detection
- Understand Middle finding

---

## 📚 Concept: Fast & Slow Pointers

### Key Ideas

- Floyd's algorithm
- Cycle detection
- Middle finding

### Real-World Applications

- Detecting infinite loops in a state machine or a linked configuration graph
- Finding the midpoint of a stream/list without knowing its length in advance

---

## 💡 Core Pattern

### Template

```python
slow = fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

### Pattern Recognition Clue
Cycle detection or finding the middle of a linked structure.

---

## 🧠 Key Insights

1. Fast moves twice as far as slow every step, so if there's a cycle, fast will eventually lap slow and they'll meet — no extra memory needed to track visited nodes.
2. Checking `fast and fast.next` (not just `fast`) prevents a crash when the list has an even number of nodes and fast reaches the very end.
3. The exact same loop shape finds the middle: when fast reaches the end, slow is sitting at the midpoint, because slow has moved exactly half as far.

---

## 📋 Practice Problems

### Problem 1: Linked List Cycle
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/linked-list-cycle/

**Problem Statement:**
Given the `head` of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if some node can be reached again by continuously following the `next` pointer.

**Examples:**
```
Input: head = [3,2,0,-4], pos = 1 (tail connects to index 1)
Output: true

Input: head = [1,2], pos = -1 (no cycle)
Output: false
```

**Constraints:**
- Number of nodes in list is in [0, 10^4]
- -10^5 <= Node.val <= 10^5

**Solution Location:** [solutions/1_linked_cycle.py](solutions/1_linked_cycle.py)
**Practice Location:** [questions/linked_cycle.py](questions/linked_cycle.py)

**Approaches to Consider:**
- Brute force: track visited nodes in a set, O(n) space
- Optimized: Floyd's fast/slow pointer, O(1) space
- Edge case: empty list or single node with no cycle

### Problem 2: Middle of the Linked List
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/middle-of-the-linked-list/

**Problem Statement:**
Given the `head` of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

**Examples:**
```
Input: head = [1,2,3,4,5]
Output: [3,4,5]

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
```

**Constraints:**
- Number of nodes in list is in [1, 100]
- 1 <= Node.val <= 100

**Solution Location:** [solutions/2_middle_list.py](solutions/2_middle_list.py)
**Practice Location:** [questions/middle_list.py](questions/middle_list.py)

**Approaches to Consider:**
- Brute force: count length, then walk to n//2, O(n) two passes
- Optimized: fast/slow pointer, O(n) one pass
- Edge case: single-node list

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Linked List Cycle)
- [ ] Solve Problem 2 (Middle of the Linked List)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- Floyd's cycle detection finds a cycle in O(1) space, beating a visited-set approach's O(n) space.
- 'Twice as fast' pointers are the general trick for 'find the middle' or 'detect a loop' in a singly linked structure.
- Always guard both `fast` and `fast.next` in the loop condition to avoid null-pointer errors.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 15](../Day-15/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

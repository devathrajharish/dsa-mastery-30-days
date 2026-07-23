# Day 13: Linked Lists

## 🎯 Learning Objectives

- Understand Node structure
- Understand Pointer manipulation
- Understand List reversal

---

## 📚 Concept: Linked Lists

### Key Ideas

- Node structure
- Pointer manipulation
- List reversal

### Real-World Applications

- Undo history in an editor, where each state points to the previous one
- Music/playlist 'next track' chaining without needing random access

---

## 💡 Core Pattern

### Template

```python
prev = None
current = head

while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node

return prev
```

### Pattern Recognition Clue
Node connections need to be changed without random access.

---

## 🧠 Key Insights

1. You must save `current.next` *before* overwriting `current.next = prev`, or you lose the rest of the list — this is the single most common linked-list bug.
2. A 'dummy' head node (a throwaway node before the real head) removes special-casing for 'is this the first node?' when building or merging lists.
3. Reversal and merging are both O(n) time, O(1) extra space (beyond the new/reused nodes) — no array copy needed, unlike array-based problems.

---

## 📋 Practice Problems

### Problem 1: Reverse Linked List
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/reverse-linked-list/

**Problem Statement:**
Given the `head` of a singly linked list, reverse the list, and return the reversed list's head.

**Examples:**
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = []
Output: []
```

**Constraints:**
- 0 <= number of nodes <= 5000
- -5000 <= Node.val <= 5000

**Solution Location:** [solutions/1_reverse_list.py](solutions/1_reverse_list.py)
**Practice Location:** [questions/reverse_list.py](questions/reverse_list.py)

**Approaches to Consider:**
- Iterative: three-pointer rewiring, O(n) time / O(1) space
- Recursive: reverse the rest, then fix the current link, O(n) time / O(n) call-stack space
- Edge case: empty list or single node

### Problem 2: Merge Two Sorted Lists
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/merge-two-sorted-lists/

**Problem Statement:**
You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list by splicing together the nodes of the first two lists. Return the head of the merged linked list.

**Examples:**
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: list1 = [], list2 = []
Output: []

Input: list1 = [], list2 = [0]
Output: [0]
```

**Constraints:**
- 0 <= number of nodes in each list <= 50
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order

**Solution Location:** [solutions/2_merge_lists.py](solutions/2_merge_lists.py)
**Practice Location:** [questions/merge_lists.py](questions/merge_lists.py)

**Approaches to Consider:**
- Brute force: collect all values, sort, rebuild a new list, O((n+m) log(n+m))
- Optimized: iterative merge with a dummy node, O(n+m)
- Edge case: one or both lists empty

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Reverse Linked List)
- [ ] Solve Problem 2 (Merge Two Sorted Lists)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- Always cache `current.next` before rewiring `current.next`, or the rest of the list becomes unreachable.
- A dummy node simplifies list-building code by eliminating 'first node' edge cases.
- Linked list problems are about careful pointer bookkeeping, not clever algorithms — trace through a small example by hand before coding.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 14](../Day-14/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

# Day 16: Stack

## 🎯 Learning Objectives

- Understand LIFO principle
- Understand Matching brackets
- Understand Undo operations

---

## 📚 Concept: Stack

### Key Ideas

- LIFO principle
- Matching brackets
- Undo operations

### Real-World Applications

- The browser back button / undo-redo stack in an editor
- Validating balanced brackets/tags in a code formatter or XML/HTML parser

---

## 💡 Core Pattern

### Template

```python
stack = []

for item in items:
    if should_push:
        stack.append(item)
    else:
        top = stack.pop()
```

### Pattern Recognition Clue
Matching, nested structures, undo operations, or LIFO behavior.

---

## 🧠 Key Insights

1. A stack is the natural fit whenever 'the most recent thing' is what you need to check or undo next — last in, first out.
2. For bracket matching, push opening brackets and pop-and-compare on closing brackets; an empty stack when you expect to pop, or a leftover stack at the end, both mean invalid input.
3. Min Stack shows a stack can track more than just values — storing the running minimum alongside each pushed value keeps `getMin()` O(1) without re-scanning.

---

## 📋 Practice Problems

### Problem 1: Valid Parentheses
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/valid-parentheses/

**Problem Statement:**
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. Brackets must close in the correct order and every open bracket must be closed by the same type.

**Examples:**
```
Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false
```

**Constraints:**
- 1 <= s.length <= 10^4
- s consists only of bracket characters

**Solution Location:** [solutions/1_valid_parentheses.py](solutions/1_valid_parentheses.py)
**Practice Location:** [questions/valid_parentheses.py](questions/valid_parentheses.py)

**Approaches to Consider:**
- Brute force: repeatedly remove matched innermost pairs until stable, O(n^2)
- Optimized: stack matching each closer to the most recent opener, O(n)
- Edge case: unmatched leftover openers at the end

### Problem 2: Min Stack
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/min-stack/

**Problem Statement:**
Design a stack that supports push, pop, top, and retrieving the minimum element, all in O(1) time.

**Examples:**
```
push(-2), push(0), push(-3)
getMin() -> -3
pop()
top() -> 0
getMin() -> -2
```

**Constraints:**
- -2^31 <= val <= 2^31 - 1
- Methods called at most 3 * 10^4 times
- pop/top/getMin always called on a non-empty stack

**Solution Location:** [solutions/2_min_stack.py](solutions/2_min_stack.py)
**Practice Location:** [questions/min_stack.py](questions/min_stack.py)

**Approaches to Consider:**
- Brute force: getMin() scans the whole stack each call, O(n) per call
- Optimized: auxiliary min-stack tracking the running minimum, O(1) per call
- Edge case: pushing a new minimum, then popping it

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Valid Parentheses)
- [ ] Solve Problem 2 (Min Stack)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- Reach for a stack whenever the problem is about nesting, matching pairs, or 'undo the last operation'.
- Bracket validity checks reduce to: push on open, pop-and-compare on close, and the stack must be empty at the end.
- You can keep auxiliary state (like a running min) alongside a stack instead of separately, to get O(1) queries.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 17](../Day-17/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

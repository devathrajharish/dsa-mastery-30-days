# 📝 Mistakes Log & Learning Journal

Use this document to track difficult problems, common mistakes, and what you learn from them.

> **Remember:** Mistakes are learning opportunities. Reviewing them is how you improve!

---

## Template for Each Entry

```
### Problem: [Problem Name]
**Difficulty:** Easy | Medium | Hard  
**Date:** [Date]  
**Pattern:** [Which pattern does this use?]  
**Leetcode/Source:** [Link]

#### My Initial Approach
[What was your first idea?]

#### Why It Failed / Was Inefficient
[What went wrong?]
- Time complexity issue?
- Logic error?
- Edge case missed?
- Misunderstood the problem?

#### Correct Insight
[What was the key realization?]

#### Correct Solution Approach
[Brief explanation of correct approach]

#### Time Complexity: [Brute Force] → [Optimized]
#### Space Complexity: [Brute Force] → [Optimized]

#### What Clue Should Help Me Next Time?
[How should I recognize this pattern immediately?]

#### Revisit Date: [When will you redo this?]
```

---

## Entries

### Problem 1: [Your First Challenging Problem]
**Difficulty:** -  
**Date:** -  
**Pattern:** -

#### My Initial Approach
[Fill this in]

#### Why It Failed / Was Inefficient
[Fill this in]

#### Correct Insight
[Fill this in]

#### Correct Solution Approach
[Fill this in]

#### Time Complexity: O(?) → O(?)
#### Space Complexity: O(?) → O(?)

#### What Clue Should Help Me Next Time?
[Fill this in]

#### Revisit Date: -

---

### Problem 2: [Your Second Challenging Problem]
**Difficulty:** -  
**Date:** -  
**Pattern:** -

#### My Initial Approach
[Fill this in]

#### Why It Failed / Was Inefficient
[Fill this in]

#### Correct Insight
[Fill this in]

#### Correct Solution Approach
[Fill this in]

#### Time Complexity: O(?) → O(?)
#### Space Complexity: O(?) → O(?)

#### What Clue Should Help Me Next Time?
[Fill this in]

#### Revisit Date: -

---

## Common Mistakes to Avoid

### Arrays & Hashing
- [ ] Forgetting to handle empty arrays
- [ ] Integer overflow (Python handles big integers, but be aware)
- [ ] Off-by-one errors in loops
- [ ] Not considering negative numbers
- [ ] Modifying input array when you shouldn't

### Sliding Window
- [ ] Wrong window expansion/contraction logic
- [ ] Forgetting to update answer while maintaining window validity
- [ ] Not handling edge cases (empty string, k > length)
- [ ] Over-complicating the shrink condition

### Binary Search
- [ ] Infinite loop with `left = mid` (should be `mid + 1`)
- [ ] Incorrect mid calculation leading to overflow
- [ ] Forgetting to handle the target not being in array
- [ ] Not correctly identifying which half to search

### Linked Lists
- [ ] Forgetting to save `next` before breaking links
- [ ] Not handling None/null checks
- [ ] Losing the head reference
- [ ] Off-by-one in fast/slow pointers

### Stack & Queue
- [ ] Stack underflow (popping from empty stack)
- [ ] Confusing stack and queue order
- [ ] Not properly managing visited states in graph problems
- [ ] Incorrect comparison in monotonic stack

### Trees
- [ ] Forgetting base case for recursion
- [ ] Modifying tree structure accidentally
- [ ] Not handling single node or empty tree
- [ ] Mixing up return value (node count vs max value)

### Graphs
- [ ] Forgetting to mark nodes as visited (infinite loops)
- [ ] Not initializing visited set/dictionary
- [ ] Wrong neighbor calculation in grid problems
- [ ] Off-by-one in row/column bounds

### Dynamic Programming
- [ ] Wrong state definition
- [ ] Incorrect base cases
- [ ] Wrong recurrence relation
- [ ] Forgetting to initialize DP array properly
- [ ] Off-by-one in array indexing

---

## Patterns of Mistakes

### Pattern 1: Off-by-One Errors
**How often:** Every week  
**Why it happens:** Quick coding without careful index checking  
**Prevention:** Always trace through examples with indices

### Pattern 2: Edge Cases
**How often:** Every other day  
**Why it happens:** Focusing on main logic, forgetting special cases  
**Prevention:** Before coding, list edge cases explicitly

### Pattern 3: Not Analyzing Complexity First
**How often:** Frequently  
**Why it happens:** Jumping straight to coding  
**Prevention:** Write brute force complexity before optimizing

---

## Spaced Repetition Revisit Schedule

**Week 1 Mistakes:** Review on Day 4, Day 7, Day 14  
**Week 2 Mistakes:** Review on Day 11, Day 15  
**Week 3 Mistakes:** Review on Day 22  
**Week 4 Mistakes:** Review on Day 30

---

## Weekly Reflection

### Week 1 Reflection
**Date:** -  
**Most common mistake:** -  
**Pattern I struggled with:** -  
**Breakthrough moment:** -  
**Next week's focus:** -

### Week 2 Reflection
**Date:** -  
**Most common mistake:** -  
**Pattern I struggled with:** -  
**Breakthrough moment:** -  
**Next week's focus:** -

### Week 3 Reflection
**Date:** -  
**Most common mistake:** -  
**Pattern I struggled with:** -  
**Breakthrough moment:** -  
**Next week's focus:** -

### Week 4 Reflection
**Date:** -  
**Most common mistake:** -  
**Pattern I struggled with:** -  
**Breakthrough moment:** -  
**Next week's focus:** -

---

## 30-Day Summary

**Date Completed:** -  
**Total Problems Solved:** -  
**Patterns Mastered:** -  
**Biggest Challenges:** -  
**Most Important Lessons:** -  
**Ready for interviews?** -

---

## Resources for Review

- **LeetCode:** https://leetcode.com (filter by pattern)
- **NeetCode Patterns:** https://neetcode.io (categorized problems)
- **GeeksforGeeks:** https://www.geeksforgeeks.org (pattern explanations)
- **AlgoExpert:** https://www.algoexpert.io (comprehensive library)

---

*Keep this log updated as you progress through the 30 days. Your future self will thank you!*

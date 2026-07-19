# Day 10: Prefix Sum

## 🎯 Learning Objectives

- Understand Prefix sum array
Understand Range sum queries
Understand Cumulative calculations

---

## 📚 Concept: Prefix Sum

### Key Ideas

- Prefix sum array
- Range sum queries
- Cumulative calculations

### Real-World Applications

- [Add real-world use cases]
- [Add more examples]

---

## 💡 Core Pattern

### Template

```python
prefix = [0]

for num in nums:
    prefix.append(prefix[-1] + num)

range_sum = prefix[right + 1] - prefix[left]
```

### Pattern Recognition Clue
Repeated range sums or cumulative calculations.

---

## 🧠 Key Insights

1. [Key insight 1]
2. [Key insight 2]
3. [Key insight 3]

---

## 📋 Practice Problems

### Problem 1: Range Sum Query - Immutable
**Difficulty:** Easy

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/1_range_sum_query.py](solutions/1_range_sum_query.py)

**Approaches to Consider:**
- Brute force solution
- Optimized approach
- Edge cases and validation

### Problem 2: Subarray Sum Equals K
**Difficulty:** Medium

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/2_subarray_sum_k.py](solutions/2_subarray_sum_k.py)

**Approaches to Consider:**
- Brute force solution
- Optimized approach
- Edge cases and validation

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1
- [ ] Solve Problem 2
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]

---

## 🎬 Next Steps

Once you complete this day:
1. Review your solutions
2. Check edge cases
3. Verify complexity analysis
4. Move to [Day 11](../Day-11/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

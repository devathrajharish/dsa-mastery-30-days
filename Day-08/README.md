# Day 08: Fixed Sliding Window

## 🎯 Learning Objectives

- Understand Fixed-size window
Understand Sliding mechanism
Understand Sum optimization

---

## 📚 Concept: Fixed Sliding Window

### Key Ideas

- Fixed-size window
- Sliding mechanism
- Sum optimization

### Real-World Applications

- [Add real-world use cases]
- [Add more examples]

---

## 💡 Core Pattern

### Template

```python
window_sum = sum(nums[:k])
best = window_sum

for right in range(k, len(nums)):
    window_sum += nums[right]
    window_sum -= nums[right - k]
    best = max(best, window_sum)
```

### Pattern Recognition Clue
A fixed-size contiguous subarray or substring.

---

## 🧠 Key Insights

1. [Key insight 1]
2. [Key insight 2]
3. [Key insight 3]

---

## 📋 Practice Problems

### Problem 1: Maximum Average Subarray I
**Difficulty:** Easy

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/1_max_avg_subarray.py](solutions/1_max_avg_subarray.py)

**Approaches to Consider:**
- Brute force solution
- Optimized approach
- Edge cases and validation

### Problem 2: Maximum Sum Subarray of Size K
**Difficulty:** Easy

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/2_max_sum_subarray.py](solutions/2_max_sum_subarray.py)

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
4. Move to [Day 09](../Day-09/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

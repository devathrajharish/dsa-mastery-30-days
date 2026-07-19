# Day 05: Two Pointers: Arrays

## 🎯 Learning Objectives

- Understand Left/right pointers
Understand In-place array manipulation
Understand Sorted array optimization

---

## 📚 Concept: Two Pointers: Arrays

### Key Ideas

- Left/right pointers
- In-place array manipulation
- Sorted array optimization

### Real-World Applications

- [Add real-world use cases]
- [Add more examples]

---

## 💡 Core Pattern

### Template

```python
left = 0

for right in range(len(nums)):
    if condition:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
```

### Pattern Recognition Clue
You need to process an array using two positions without extra nested loops.

---

## 🧠 Key Insights

1. [Key insight 1]
2. [Key insight 2]
3. [Key insight 3]

---

## 📋 Practice Problems

### Problem 1: Move Zeroes
**Difficulty:** Easy

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/1_move_zeroes.py](solutions/1_move_zeroes.py)

**Approaches to Consider:**
- Brute force solution
- Optimized approach
- Edge cases and validation

### Problem 2: Remove Duplicates from Sorted Array
**Difficulty:** Easy

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/2_remove_duplicates.py](solutions/2_remove_duplicates.py)

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
4. Move to [Day 06](../Day-06/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

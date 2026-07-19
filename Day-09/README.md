# Day 09: Variable Sliding Window

## 🎯 Learning Objectives

- Understand Dynamic window size
Understand Expand/shrink logic
Understand Valid window conditions

---

## 📚 Concept: Variable Sliding Window

### Key Ideas

- Dynamic window size
- Expand/shrink logic
- Valid window conditions

### Real-World Applications

- [Add real-world use cases]
- [Add more examples]

---

## 💡 Core Pattern

### Template

```python
left = 0

for right in range(len(nums)):
    # Add right element

    while window_is_invalid:
        # Remove left element
        left += 1

    # Update answer
```

### Pattern Recognition Clue
Longest/shortest valid contiguous substring or subarray.

---

## 🧠 Key Insights

1. [Key insight 1]
2. [Key insight 2]
3. [Key insight 3]

---

## 📋 Practice Problems

### Problem 1: Longest Substring Without Repeating Characters
**Difficulty:** Medium

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/1_longest_substring.py](solutions/1_longest_substring.py)

**Approaches to Consider:**
- Brute force solution
- Optimized approach
- Edge cases and validation

### Problem 2: Longest Repeating Character Replacement
**Difficulty:** Medium

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/2_character_replacement.py](solutions/2_character_replacement.py)

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
4. Move to [Day 10](../Day-10/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

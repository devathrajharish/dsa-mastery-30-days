# Day 03: Hash Maps

## 🎯 Learning Objectives

- Understand Python dictionaries - Key-value lookup
Understand Complement technique
Understand Frequency counting

---

## 📚 Concept: Hash Maps

### Key Ideas

- Python dictionaries - Key-value lookup
- Complement technique
- Frequency counting

### Real-World Applications

- [Add real-world use cases]
- [Add more examples]

---

## 💡 Core Pattern

### Template

```python
seen = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        return [seen[complement], i]

    seen[num] = i
```

### Pattern Recognition Clue
Storing previously seen information can eliminate a nested loop.

---

## 🧠 Key Insights

1. [Key insight 1]
2. [Key insight 2]
3. [Key insight 3]

---

## 📋 Practice Problems

### Problem 1: Two Sum
**Difficulty:** Easy

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/1_two_sum.py](solutions/1_two_sum.py)

**Approaches to Consider:**
- Brute force solution
- Optimized approach
- Edge cases and validation

### Problem 2: Majority Element
**Difficulty:** Easy

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/2_majority_element.py](solutions/2_majority_element.py)

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
4. Move to [Day 04](../Day-04/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

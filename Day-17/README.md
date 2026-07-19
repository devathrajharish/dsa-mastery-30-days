# Day 17: Monotonic Stack

## 🎯 Learning Objectives

- Understand Ordered element storage
Understand Next greater element
Understand O(n) solution for O(n²) problem

---

## 📚 Concept: Monotonic Stack

### Key Ideas

- Ordered element storage
- Next greater element
- O(n) solution for O(n²) problem

### Real-World Applications

- [Add real-world use cases]
- [Add more examples]

---

## 💡 Core Pattern

### Template

```python
stack = []

for i, value in enumerate(nums):
    while stack and nums[stack[-1]] < value:
        index = stack.pop()
        # Process answer for index

    stack.append(i)
```

### Pattern Recognition Clue
Next greater/smaller element.

---

## 🧠 Key Insights

1. [Key insight 1]
2. [Key insight 2]
3. [Key insight 3]

---

## 📋 Practice Problems

### Problem 1: Daily Temperatures
**Difficulty:** Medium

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/1_daily_temps.py](solutions/1_daily_temps.py)

**Approaches to Consider:**
- Brute force solution
- Optimized approach
- Edge cases and validation

### Problem 2: Next Greater Element I
**Difficulty:** Easy

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/2_next_greater.py](solutions/2_next_greater.py)

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
4. Move to [Day 18](../Day-18/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

# Day 24: Intervals

## 🎯 Learning Objectives

- Understand Overlapping detection
Understand Interval merging
Understand Sort by start point

---

## 📚 Concept: Intervals

### Key Ideas

- Overlapping detection
- Interval merging
- Sort by start point

### Real-World Applications

- [Add real-world use cases]
- [Add more examples]

---

## 💡 Core Pattern

### Template

```python
intervals.sort(key=lambda x: x[0])
merged = []

for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])
```

### Pattern Recognition Clue
Overlapping ranges, meetings, schedules, start/end times.

---

## 🧠 Key Insights

1. [Key insight 1]
2. [Key insight 2]
3. [Key insight 3]

---

## 📋 Practice Problems

### Problem 1: Merge Intervals
**Difficulty:** Medium

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/1_merge_intervals.py](solutions/1_merge_intervals.py)

**Approaches to Consider:**
- Brute force solution
- Optimized approach
- Edge cases and validation

### Problem 2: Insert Interval
**Difficulty:** Medium

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/2_insert_interval.py](solutions/2_insert_interval.py)

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
4. Move to [Day 25](../Day-25/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

# Day 23: Heap / Priority Queue

## 🎯 Learning Objectives

- Understand Min-heap (Python default)
Understand Heapify operations
Understand K-smallest/largest problems

---

## 📚 Concept: Heap / Priority Queue

### Key Ideas

- Min-heap (Python default)
- Heapify operations
- K-smallest/largest problems

### Real-World Applications

- [Add real-world use cases]
- [Add more examples]

---

## 💡 Core Pattern

### Template

```python
import heapq

heap = []

for value in nums:
    heapq.heappush(heap, value)

    if len(heap) > k:
        heapq.heappop(heap)
```

### Pattern Recognition Clue
Top K, Kth largest/smallest, or repeatedly selecting min/max.

---

## 🧠 Key Insights

1. [Key insight 1]
2. [Key insight 2]
3. [Key insight 3]

---

## 📋 Practice Problems

### Problem 1: Kth Largest Element in an Array
**Difficulty:** Medium

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/1_kth_largest.py](solutions/1_kth_largest.py)

**Approaches to Consider:**
- Brute force solution
- Optimized approach
- Edge cases and validation

### Problem 2: Top K Frequent Elements
**Difficulty:** Medium

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/2_top_k_frequent.py](solutions/2_top_k_frequent.py)

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
4. Move to [Day 24](../Day-24/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

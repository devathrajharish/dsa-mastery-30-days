# Day 07: Week 1 Revision

## 🎯 Learning Objectives

- Review and apply Arrays
- Review and apply Hash Set
- Review and apply Hash Map
- Review and apply Frequency counting
- Review and apply Two Pointers

---

## 📚 Concept: Week 1 Revision

Week 1 covered five foundational patterns: array traversal and Big-O (Day 01), hash sets for existence checks (Day 02), hash maps for key-value/complement lookups (Day 03), frequency counting with `Counter` (Day 04), and two pointers on arrays and strings (Day 05-06). Today has no new concept — the goal is to prove you can *recognize* which of these five patterns a brand-new problem needs, without being told which day it belongs to.

### Patterns to Review

- Arrays
- Hash Set
- Hash Map
- Frequency counting
- Two Pointers

---

## 💡 Core Pattern

### Template

Challenge: Pick 3 unseen Easy/Medium problems.

For each problem, write:
```
Brute Force:
Pattern:
Optimized Approach:
Time Complexity:
Space Complexity:
```

### Pattern Recognition Clue
Mixed problems - identify pattern before solving!

---

## 🧠 Key Insights

1. If you find yourself writing a nested loop to check 'have I seen this', that's the signal to reach for a hash set/map instead.
2. If the array is sorted, or you're comparing from both ends, that's the signal for two pointers instead of extra space.
3. The hardest part of Week 1 isn't the code — it's the 10 seconds before you write any code where you name the pattern.

---

## 📋 Practice Problems

Unlike other days, this is a **revision day** — there's no single fixed
problem. Pick unseen Easy/Medium problems that exercise the patterns
above, then fill in the slots below.

### Slot 1: Mixed Problem 1
**Difficulty:** Medium

**Instructions:**
Pick an unseen problem best solved with a **Hash Set or Hash Map** (Day 02-03 patterns).

**Solution Location:** [solutions/1_mixed_problem.py](solutions/1_mixed_problem.py)
**Practice Location:** [questions/mixed_problem_1.py](questions/mixed_problem_1.py)

### Slot 2: Mixed Problem 2
**Difficulty:** Medium

**Instructions:**
Pick an unseen problem best solved with **Frequency Counting** (Day 04 pattern).

**Solution Location:** [solutions/2_mixed_problem.py](solutions/2_mixed_problem.py)
**Practice Location:** [questions/mixed_problem_2.py](questions/mixed_problem_2.py)

### Slot 3: Mixed Problem 3
**Difficulty:** Medium

**Instructions:**
Pick an unseen problem best solved with **Two Pointers** on an array or string (Day 05-06 pattern).

**Solution Location:** [solutions/3_mixed_problem.py](solutions/3_mixed_problem.py)
**Practice Location:** [questions/mixed_problem_3.py](questions/mixed_problem_3.py)

---

## ✅ Daily Checklist

- [ ] Review all patterns from this section
- [ ] Pick and solve Slot 1 (Mixed Problem 1)
- [ ] Pick and solve Slot 2 (Mixed Problem 2)
- [ ] Pick and solve Slot 3 (Mixed Problem 3)
- [ ] Write a one-line 'pattern recognition clue' for each problem solved
- [ ] Record any mistakes in the mistakes log

---

## 📝 Key Takeaways

- Pattern recognition is a skill you build by re-solving problems without hints, not by memorizing solutions.
- Hash-based and two-pointer patterns cover a surprisingly large share of 'Easy' array/string problems.
- Writing down brute force first, even when you already see the optimized approach, cements the time/space trade-off.

---

## 🎬 Next Steps

Once you complete this day:
1. Fill in each slot's `solutions/` and `questions/` file with the problem you picked
2. Review your solutions and check edge cases
3. Verify complexity analysis
4. Move to [Day 08](../Day-08/README.md)

**Time Goal:** 60 minutes

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

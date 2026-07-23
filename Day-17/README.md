# Day 17: Monotonic Stack

## 🎯 Learning Objectives

- Understand Ordered element storage
- Understand Next greater element
- Understand O(n) solution for O(n²) problem

---

## 📚 Concept: Monotonic Stack

### Key Ideas

- Ordered element storage
- Next greater element
- O(n) solution for O(n²) problem

### Real-World Applications

- Stock span problems: how many consecutive prior days had a lower price
- Computing 'next higher priority task' style lookups in a scheduling system

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

1. The stack stores indices in decreasing order of value — each time a bigger value shows up, it 'resolves' every smaller value still waiting on the stack, in one pass.
2. Every index is pushed once and popped at most once, which is why a naive-looking nested `while` inside a `for` still totals O(n), not O(n^2).
3. The same shape answers both Daily Temperatures (distance to next greater) and Next Greater Element I (value of next greater) — only what you store when popping changes.

---

## 📋 Practice Problems

### Problem 1: Daily Temperatures
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/daily-temperatures/

**Problem Statement:**
Given an array of integers `temperatures` representing daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i`-th day to get a warmer temperature. If there is no future day for which this is possible, `answer[i] == 0`.

**Examples:**
```
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Constraints:**
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

**Solution Location:** [solutions/1_daily_temps.py](solutions/1_daily_temps.py)
**Practice Location:** [questions/daily_temps.py](questions/daily_temps.py)

**Approaches to Consider:**
- Brute force: for each day, scan forward for a warmer day, O(n^2)
- Optimized: monotonic decreasing stack of indices, O(n)
- Edge case: strictly decreasing temperatures (all zeros)

### Problem 2: Next Greater Element I
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/next-greater-element-i/

**Problem Statement:**
The next greater element of some element `x` in an array is the first greater element that is to the right of `x` in the same array. You are given two distinct 0-indexed integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`. For each `nums1[i]`, find the next greater element in `nums2`. If it does not exist, return `-1` for this number.

**Examples:**
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
```

**Constraints:**
- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10^4
- All integers in nums1 and nums2 are unique
- nums1 is a subset of nums2

**Solution Location:** [solutions/2_next_greater.py](solutions/2_next_greater.py)
**Practice Location:** [questions/next_greater.py](questions/next_greater.py)

**Approaches to Consider:**
- Brute force: for each nums1 element, scan nums2 forward, O(n*m)
- Optimized: monotonic stack precomputing next-greater for all of nums2, O(n+m)
- Edge case: element is the maximum in nums2 (answer -1)

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Daily Temperatures)
- [ ] Solve Problem 2 (Next Greater Element I)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- A monotonic stack turns 'next greater element for every position' from O(n^2) into O(n).
- Amortized analysis matters: each element is pushed once and popped once, bounding total work to O(n) even with a nested loop.
- Store indices (not values) on the stack when you need to compute a distance/position in the answer.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 18](../Day-18/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

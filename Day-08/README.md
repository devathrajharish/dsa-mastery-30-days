# Day 08: Fixed Sliding Window

## 🎯 Learning Objectives

- Understand Fixed-size window
- Understand Sliding mechanism
- Understand Sum optimization

---

## 📚 Concept: Fixed Sliding Window

### Key Ideas

- Fixed-size window
- Sliding mechanism
- Sum optimization

### Real-World Applications

- Computing a rolling average over the last N sensor readings
- Rate limiting: counting requests in the last fixed-size time window

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

1. Once you have the sum of the first window, every subsequent window differs by exactly one 'add' and one 'remove' — recomputing from scratch is wasted work.
2. The window size never changes here, which is what separates this from Day 09's variable window — you always add index `right` and drop index `right - k`.
3. This pattern generalizes beyond sums to any aggregate that can be updated incrementally (max via deque, distinct-count via a frequency map, etc.).

---

## 📋 Practice Problems

### Problem 1: Maximum Average Subarray I
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/maximum-average-subarray-i/

**Problem Statement:**
Given an integer array `nums` and an integer `k`, find a contiguous subarray of length `k` with the maximum average value, and return this value. Any answer within `10^-5` of the actual answer is accepted.

**Examples:**
```
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Max average is (12-5-6+50)/4 = 51/4 = 12.75

Input: nums = [5], k = 1
Output: 5.0
```

**Constraints:**
- n == nums.length
- 1 <= k <= n <= 10^5
- -10^4 <= nums[i] <= 10^4

**Solution Location:** [solutions/1_max_avg_subarray.py](solutions/1_max_avg_subarray.py)
**Practice Location:** [questions/max_avg_subarray.py](questions/max_avg_subarray.py)

**Approaches to Consider:**
- Brute force: recompute the sum for every window, O(n*k)
- Optimized: sliding window sum, O(n)
- Edge case: k == n (only one window)

### Problem 2: Maximum Sum Subarray of Size K
**Difficulty:** Easy
**LeetCode:** https://www.geeksforgeeks.org/maximum-sum-subarray-of-size-k/

**Problem Statement:**
Given an array of positive integers `nums` and a positive integer `k`, find the maximum sum of any contiguous subarray of size exactly `k`.

**Examples:**
```
Input: nums = [2,1,5,1,3,2], k = 3
Output: 9
Explanation: Subarray [5,1,3] has the maximum sum 9.

Input: nums = [2,3,4,1,5], k = 2
Output: 7
```

**Constraints:**
- 1 <= k <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

**Solution Location:** [solutions/2_max_sum_subarray.py](solutions/2_max_sum_subarray.py)
**Practice Location:** [questions/max_sum_subarray.py](questions/max_sum_subarray.py)

**Approaches to Consider:**
- Brute force: recompute the sum for every window, O(n*k)
- Optimized: sliding window sum, O(n)
- Edge case: k equals array length

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Maximum Average Subarray I)
- [ ] Solve Problem 2 (Maximum Sum Subarray of Size K)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- A fixed window turns O(n*k) brute force into O(n) by reusing the previous window's sum.
- The sliding update is always 'add the new right element, remove the element that just fell out of the window'.
- This is the simplest sliding-window shape — master it before the variable-size version in Day 09.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 09](../Day-09/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

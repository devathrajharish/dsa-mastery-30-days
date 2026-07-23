# Day 10: Prefix Sum

## 🎯 Learning Objectives

- Understand Prefix sum array
- Understand Range sum queries
- Understand Cumulative calculations

---

## 📚 Concept: Prefix Sum

### Key Ideas

- Prefix sum array
- Range sum queries
- Cumulative calculations

### Real-World Applications

- Answering 'total sales between date X and Y' instantly from a running daily-totals table
- Computing cumulative distribution (percentile) lookups without re-summing each time

---

## 💡 Core Pattern

### Template

```python
prefix = [0]

for num in nums:
    prefix.append(prefix[-1] + num)

range_sum = prefix[right + 1] - prefix[left]
```

### Pattern Recognition Clue
Repeated range sums or cumulative calculations.

---

## 🧠 Key Insights

1. Precomputing prefix sums costs O(n) once, but turns every subsequent range-sum query into O(1) — a huge win when there are many queries.
2. `prefix[i]` represents the sum of everything *before* index i, which is why `range_sum = prefix[right+1] - prefix[left]` (not `prefix[right] - prefix[left]`) gives the inclusive sum from left to right.
3. Subarray Sum Equals K flips the idea around: instead of querying known ranges, you use a hash map of prefix-sum counts to discover how many ranges sum to k.

---

## 📋 Practice Problems

### Problem 1: Range Sum Query - Immutable
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/range-sum-query-immutable/

**Problem Statement:**
Given an integer array `nums`, handle multiple queries of the following type: calculate the sum of the elements of `nums` between indices `left` and `right` inclusive, where `left <= right`.

**Examples:**
```
Input: nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1   (-2 + 0 + 3)
sumRange(2, 5) -> -1  (3 + -5 + 2 + -1)
sumRange(0, 5) -> -3
```

**Constraints:**
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
- 0 <= left <= right < nums.length
- At most 10^4 calls to sumRange

**Solution Location:** [solutions/1_range_sum_query.py](solutions/1_range_sum_query.py)
**Practice Location:** [questions/range_sum_query.py](questions/range_sum_query.py)

**Approaches to Consider:**
- Brute force: sum(nums[left:right+1]) on every call, O(n) per query
- Optimized: precompute a prefix sum array once, O(1) per query
- Edge case: left == right (single element)

### Problem 2: Subarray Sum Equals K
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/subarray-sum-equals-k/

**Problem Statement:**
Given an array of integers `nums` and an integer `k`, return the total number of contiguous subarrays whose sum equals `k`.

**Examples:**
```
Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2
Explanation: [1,2] and [3] both sum to 3.
```

**Constraints:**
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

**Solution Location:** [solutions/2_subarray_sum_k.py](solutions/2_subarray_sum_k.py)
**Practice Location:** [questions/subarray_sum_k.py](questions/subarray_sum_k.py)

**Approaches to Consider:**
- Brute force: sum every subarray, O(n^2)
- Optimized: running prefix sum + hash map of prefix-sum counts, O(n)
- Edge case: negative numbers in nums

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Range Sum Query - Immutable)
- [ ] Solve Problem 2 (Subarray Sum Equals K)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- If you'll query range sums more than once, precompute a prefix sum array first.
- Watch the off-by-one: prefix arrays are usually built with a leading 0 so `prefix[i]` is the sum of the first i elements.
- Combining prefix sums with a hash map (count of each prefix value seen) unlocks O(n) solutions to 'how many subarrays sum to k' problems.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 11](../Day-11/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

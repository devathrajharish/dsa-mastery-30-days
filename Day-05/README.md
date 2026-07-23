# Day 05: Two Pointers: Arrays

## 🎯 Learning Objectives

- Understand Left/right pointers
- Understand In-place array manipulation
- Understand Sorted array optimization

---

## 📚 Concept: Two Pointers: Arrays

### Key Ideas

- Left/right pointers
- In-place array manipulation
- Sorted array optimization

### Real-World Applications

- Compacting a list in-place (e.g. removing deleted rows without allocating a new array)
- De-duplicating a sorted result set from a database query before returning it to the client

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

1. `left` marks the boundary of the 'processed/kept' region; `right` explores ahead — this single-pass shape replaces most O(n^2) rearrangement code.
2. In-place two-pointer swaps preserve relative order only if you swap rather than overwrite — that's why Move Zeroes swaps instead of just writing 0.
3. Sorted input is what makes Remove Duplicates solvable with two pointers in one pass: duplicates are always adjacent.

---

## 📋 Practice Problems

### Problem 1: Move Zeroes
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/move-zeroes/

**Problem Statement:**
Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements. This must be done in-place without making a copy of the array.

**Examples:**
```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]
```

**Constraints:**
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

**Solution Location:** [solutions/1_move_zeroes.py](solutions/1_move_zeroes.py)
**Practice Location:** [questions/move_zeroes.py](questions/move_zeroes.py)

**Approaches to Consider:**
- Brute force: build a new array of non-zeros then pad with zeros, O(n) extra space
- Optimized: two-pointer in-place swap, O(1) extra space
- Edge case: all zeros or no zeros

### Problem 2: Remove Duplicates from Sorted Array
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/

**Problem Statement:**
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of elements should be kept. Return `k`, the number of unique elements, after placing them at the front of `nums`.

**Examples:**
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
```

**Constraints:**
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order

**Solution Location:** [solutions/2_remove_duplicates.py](solutions/2_remove_duplicates.py)
**Practice Location:** [questions/remove_duplicates.py](questions/remove_duplicates.py)

**Approaches to Consider:**
- Brute force: build a deduplicated list with a set (loses in-place guarantee), O(n)
- Optimized: two-pointer in-place overwrite, O(1) extra space
- Edge case: all elements identical

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Move Zeroes)
- [ ] Solve Problem 2 (Remove Duplicates from Sorted Array)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- Two pointers turn many O(n^2) rearrangement problems into O(n) with O(1) extra space.
- The 'slow' pointer tracks where the next valid element should go; the 'fast' pointer just scans forward.
- Sortedness is a hint: adjacent duplicates or a monotonic condition often means a two-pointer scan will work.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 06](../Day-06/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

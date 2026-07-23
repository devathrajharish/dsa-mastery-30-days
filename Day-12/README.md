# Day 12: Modified Binary Search

## 🎯 Learning Objectives

- Understand Rotated sorted arrays
- Understand Finding pivot
- Understand Conditional space elimination

---

## 📚 Concept: Modified Binary Search

### Key Ideas

- Rotated sorted arrays
- Finding pivot
- Conditional space elimination

### Real-World Applications

- Searching a circular buffer/log file that wraps around after reaching capacity
- Finding the point where a version history 'restarted' numbering after a rollback

---

## 💡 Core Pattern

### Template

```python
# Determine which half is sorted
# Decide which half contains target
# Adjust search boundaries accordingly
```

### Pattern Recognition Clue
Sorted array with a twist or unknown pivot point.

---

## 🧠 Key Insights

1. In a rotated sorted array, at least one half of any given `[left, right]` window is always properly sorted — that half is what you use to decide where the target could be.
2. Once you know which half is sorted, checking whether target falls within that half's range tells you which side to keep, exactly like normal binary search's elimination step.
3. Finding the minimum is really finding the rotation pivot itself — comparing `nums[mid]` to `nums[right]` tells you whether the pivot is to the left or right of mid.

---

## 📋 Practice Problems

### Problem 1: Search in Rotated Sorted Array
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/search-in-rotated-sorted-array/

**Problem Statement:**
There is an integer array `nums` sorted in ascending order (with distinct values), possibly rotated at an unknown pivot. Given the rotated array `nums` and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not. You must write an algorithm with O(log n) runtime complexity.

**Examples:**
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

**Constraints:**
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique
- nums is an ascending array possibly rotated

**Solution Location:** [solutions/1_search_rotated.py](solutions/1_search_rotated.py)
**Practice Location:** [questions/search_rotated.py](questions/search_rotated.py)

**Approaches to Consider:**
- Brute force: linear scan, O(n)
- Optimized: modified binary search identifying the sorted half, O(log n)
- Edge case: array not rotated at all, or rotated at index 0

### Problem 2: Find Minimum in Rotated Sorted Array
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

**Problem Statement:**
Given the sorted rotated array `nums` of unique elements, return the minimum element of this array. You must write an algorithm that runs in O(log n) time.

**Examples:**
```
Input: nums = [3,4,5,1,2]
Output: 1

Input: nums = [4,5,6,7,0,1,2]
Output: 0

Input: nums = [11,13,15,17]
Output: 11
```

**Constraints:**
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All values of nums are unique

**Solution Location:** [solutions/2_min_rotated.py](solutions/2_min_rotated.py)
**Practice Location:** [questions/min_rotated.py](questions/min_rotated.py)

**Approaches to Consider:**
- Brute force: linear scan with min(), O(n)
- Optimized: binary search comparing mid to right, O(log n)
- Edge case: array not rotated at all

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Search in Rotated Sorted Array)
- [ ] Solve Problem 2 (Find Minimum in Rotated Sorted Array)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- Rotated-sorted-array problems still support O(log n) search — you just add one extra check to find which half is sorted.
- Compare `nums[mid]` against an endpoint (`nums[left]` or `nums[right]`) to determine sortedness of a half, not against the target.
- The 'find minimum' and 'search rotated array' problems share the same core idea: locate the pivot by half-elimination.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 13](../Day-13/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

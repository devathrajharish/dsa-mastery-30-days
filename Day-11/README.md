# Day 11: Binary Search

## 🎯 Learning Objectives

- Understand Sorted array assumption
- Understand Half-space elimination
- Understand Mid calculation

---

## 📚 Concept: Binary Search

### Key Ideas

- Sorted array assumption
- Half-space elimination
- Mid calculation

### Real-World Applications

- Looking up a word in a sorted dictionary or a key in a sorted database index
- Autocomplete/version lookup: finding the first release that introduced a feature

---

## 💡 Core Pattern

### Template

```python
left, right = 0, len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

return -1
```

### Pattern Recognition Clue
Sorted input or the ability to eliminate half the search space.

---

## 🧠 Key Insights

1. Binary search doesn't require finding the target directly — it requires a yes/no condition that splits the space into 'definitely not here' and 'maybe here', letting you discard half each time.
2. `left <= right` (not `<`) matters: it's what lets the loop check the last remaining candidate instead of stopping one early.
3. Search Insert Position shows binary search doesn't need an exact match — the loop naturally lands `left` at the correct insertion point when no match is found.

---

## 📋 Practice Problems

### Problem 1: Binary Search
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/binary-search/

**Problem Statement:**
Given a sorted (ascending), distinct-valued array `nums` and an integer `target`, write a function that searches for `target`. If it exists, return its index; otherwise return `-1`. You must write an algorithm with O(log n) runtime complexity.

**Examples:**
```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
```

**Constraints:**
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All values in nums are unique, sorted ascending

**Solution Location:** [solutions/1_binary_search.py](solutions/1_binary_search.py)
**Practice Location:** [questions/binary_search.py](questions/binary_search.py)

**Approaches to Consider:**
- Brute force: linear scan, O(n)
- Optimized: classic binary search, O(log n)
- Edge case: target smaller/larger than every element

### Problem 2: Search Insert Position
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/search-insert-position/

**Problem Statement:**
Given a sorted array of distinct integers `nums` and a `target` value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.

**Examples:**
```
Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4
```

**Constraints:**
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i], target <= 10^4
- nums contains distinct values sorted ascending

**Solution Location:** [solutions/2_search_insert_pos.py](solutions/2_search_insert_pos.py)
**Practice Location:** [questions/search_insert_pos.py](questions/search_insert_pos.py)

**Approaches to Consider:**
- Brute force: linear scan for the first element >= target, O(n)
- Optimized: binary search returning the left pointer, O(log n)
- Edge case: target larger than every element (insert at end)

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Binary Search)
- [ ] Solve Problem 2 (Search Insert Position)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- Binary search is O(log n) because each comparison discards half of the remaining candidates.
- The loop invariant `left <= right` and the exact mid formula are the two places off-by-one bugs hide — write them the same way every time.
- When there's no exact match, `left` ends up pointing at the correct insertion index — useful beyond just found/not-found problems.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 12](../Day-12/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

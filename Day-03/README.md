# Day 03: Hash Maps

## 🎯 Learning Objectives

- Understand Python dictionaries - Key-value lookup
- Understand Complement technique
- Understand Frequency counting

---

## 📚 Concept: Hash Maps

### Key Ideas

- Python dictionaries - Key-value lookup
- Complement technique
- Frequency counting

### Real-World Applications

- Looking up a user's session data by token in O(1)
- Counting word frequency for a search/autocomplete index

---

## 💡 Core Pattern

### Template

```python
seen = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        return [seen[complement], i]

    seen[num] = i
```

### Pattern Recognition Clue
Storing previously seen information can eliminate a nested loop.

---

## 🧠 Key Insights

1. A dict is a set that also remembers a value — use it whenever you need the index/count of what you've seen, not just whether you've seen it.
2. The 'complement' trick (target - num) turns an O(n^2) pair search into a single O(n) pass by checking 'have I already seen what I need?'
3. Majority Element shows a different family of trick entirely: Boyer-Moore voting solves it in O(1) space when a dict would use O(n).

---

## 📋 Practice Problems

### Problem 1: Two Sum
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/two-sum/

**Problem Statement:**
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. Each input has exactly one solution, and you may not use the same element twice. Return the answer in any order.

**Examples:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
```

**Constraints:**
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Exactly one valid answer exists

**Solution Location:** [solutions/1_two_sum.py](solutions/1_two_sum.py)
**Practice Location:** [questions/two_sum.py](questions/two_sum.py)

**Approaches to Consider:**
- Brute force: check every pair, O(n^2)
- Optimized: hash map storing value -> index, O(n)
- Edge case: duplicate values that sum to target

### Problem 2: Majority Element
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/majority-element/

**Problem Statement:**
Given an array `nums` of size `n`, return the majority element — the element that appears more than `n / 2` times. You may assume the majority element always exists.

**Examples:**
```
Input: nums = [3,2,3]
Output: 3

Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

**Constraints:**
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9
- A majority element always exists

**Solution Location:** [solutions/2_majority_element.py](solutions/2_majority_element.py)
**Practice Location:** [questions/majority_element.py](questions/majority_element.py)

**Approaches to Consider:**
- Brute force: count with a hash map then find max, O(n) time / O(n) space
- Optimized: Boyer-Moore voting, O(n) time / O(1) space
- Edge case: single-element array

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Two Sum)
- [ ] Solve Problem 2 (Majority Element)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- When you need value AND position/count, use a dict instead of a set.
- Complement lookups (target - num) are the core of many 'two elements that satisfy X' problems.
- Not every counting problem needs a hash map — check if a voting/math trick removes the extra space.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 04](../Day-04/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

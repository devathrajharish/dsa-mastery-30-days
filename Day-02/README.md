# Day 02: Hash Sets

## 🎯 Learning Objectives

- Understand Python `set` - O(1) average lookup
- Understand Eliminating repeated searches
- Understand Membership testing

---

## 📚 Concept: Hash Sets

### Key Ideas

- Python `set` - O(1) average lookup
- Eliminating repeated searches
- Membership testing

### Real-World Applications

- Deduplicating user IDs in a stream of event logs
- Checking whether a username/email is already registered before insert

---

## 💡 Core Pattern

### Template

```python
seen = set()

for num in nums:
    if num in seen:
        return True
    seen.add(num)

return False
```

### Pattern Recognition Clue
You need fast existence or duplicate checking.

---

## 🧠 Key Insights

1. A `set` trades O(n) memory for O(1) average membership checks — almost always worth it when you'd otherwise re-scan the array.
2. Sets only tell you *whether* something was seen, not *where* — reach for a dict (Day 03) when you need the index/count too.
3. Math tricks (sum formula, XOR) can beat a hash set to O(1) space when the problem has structure like 'exactly one number in a known range is missing'.

---

## 📋 Practice Problems

### Problem 1: Contains Duplicate
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/contains-duplicate/

**Problem Statement:**
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**Examples:**
```
Input: nums = [1,2,3,1]
Output: true

Input: nums = [1,2,3,4]
Output: false

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

**Constraints:**
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

**Solution Location:** [solutions/1_contains_duplicate.py](solutions/1_contains_duplicate.py)
**Practice Location:** [questions/contains_duplicate.py](questions/contains_duplicate.py)

**Approaches to Consider:**
- Brute force: compare every pair, O(n^2)
- Optimized: hash set membership check, O(n)
- Edge case: empty/single-element array

### Problem 2: Missing Number
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/missing-number/

**Problem Statement:**
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in that range that is missing from the array.

**Examples:**
```
Input: nums = [3,0,1]
Output: 2

Input: nums = [0,1]
Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
```

**Constraints:**
- n == nums.length
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All numbers in nums are unique

**Solution Location:** [solutions/2_missing_number.py](solutions/2_missing_number.py)
**Practice Location:** [questions/missing_number.py](questions/missing_number.py)

**Approaches to Consider:**
- Brute force: hash set of expected range minus seen values, O(n) space
- Optimized: Gauss sum formula, O(1) space
- Edge case: missing value is 0 or n

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Contains Duplicate)
- [ ] Solve Problem 2 (Missing Number)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- Hash sets turn 'have I seen this before?' into an O(1) check instead of an O(n) re-scan.
- Look for extra structure (contiguous range, known count) before reaching for a set — sometimes math is both faster and uses less space.
- Two totally different tools (a set vs. a sum formula) can solve 'find the odd one out' problems — pick based on the constraints.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 03](../Day-03/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

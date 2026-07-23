# Day 09: Variable Sliding Window

## 🎯 Learning Objectives

- Understand Dynamic window size
- Understand Expand/shrink logic
- Understand Valid window conditions

---

## 📚 Concept: Variable Sliding Window

### Key Ideas

- Dynamic window size
- Expand/shrink logic
- Valid window conditions

### Real-World Applications

- Finding the smallest log window containing all required event types
- Auto-suggest: finding the longest run of unique recently-typed characters

---

## 💡 Core Pattern

### Template

```python
left = 0

for right in range(len(nums)):
    # Add right element

    while window_is_invalid:
        # Remove left element
        left += 1

    # Update answer
```

### Pattern Recognition Clue
Longest/shortest valid contiguous substring or subarray.

---

## 🧠 Key Insights

1. Unlike Day 08's fixed window, `left` only moves when the window becomes invalid — both pointers still only move forward, giving O(n) total work (amortized two-pointer).
2. The 'invalid' condition is problem-specific: a repeated character (Longest Substring Without Repeating Characters) or too many characters needing replacement (Character Replacement).
3. You don't need to shrink the window back down after finding a valid answer in Character Replacement — keeping the max window size ever achieved is enough, since a smaller valid window can't beat a longer invalid-turned-valid one.

---

## 📋 Practice Problems

### Problem 1: Longest Substring Without Repeating Characters
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

**Problem Statement:**
Given a string `s`, find the length of the longest substring without repeating characters.

**Examples:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc".

Input: s = "bbbbb"
Output: 1

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke".
```

**Constraints:**
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces

**Solution Location:** [solutions/1_longest_substring.py](solutions/1_longest_substring.py)
**Practice Location:** [questions/longest_substring.py](questions/longest_substring.py)

**Approaches to Consider:**
- Brute force: check every substring for repeats, O(n^3) or O(n^2) with a set
- Optimized: sliding window with a set/dict of last-seen index, O(n)
- Edge case: empty string

### Problem 2: Longest Repeating Character Replacement
**Difficulty:** Medium
**LeetCode:** https://leetcode.com/problems/longest-repeating-character-replacement/

**Problem Statement:**
Given a string `s` consisting of uppercase English letters and an integer `k`, you can choose up to `k` characters and change each to any uppercase letter. Return the length of the longest substring containing the same letter you can get after performing these operations.

**Examples:**
```
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's or two 'B's to get "AAAA" or "BBBB".

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace one 'A' to get "AABBBBA" -> substring "BBBB".
```

**Constraints:**
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters
- 0 <= k <= s.length

**Solution Location:** [solutions/2_character_replacement.py](solutions/2_character_replacement.py)
**Practice Location:** [questions/character_replacement.py](questions/character_replacement.py)

**Approaches to Consider:**
- Brute force: check every substring, count max-frequency letter, O(n^2)
- Optimized: sliding window tracking max frequency in window, O(n)
- Edge case: k >= s.length (whole string is valid)

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Longest Substring Without Repeating Characters)
- [ ] Solve Problem 2 (Longest Repeating Character Replacement)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- Variable windows expand with `right` and only contract with `left` when a validity condition breaks.
- Because each pointer only moves forward, the total work across the whole loop is still O(n), not O(n^2).
- Track the best answer (max/min length) every time the window is valid, not just when it shrinks.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 10](../Day-10/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

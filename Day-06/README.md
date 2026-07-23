# Day 06: Two Pointers: Strings

## 🎯 Learning Objectives

- Understand Palindrome checking
- Understand Two-pointer from both ends
- Understand String manipulation

---

## 📚 Concept: Two Pointers: Strings

### Key Ideas

- Palindrome checking
- Two-pointer from both ends
- String manipulation

### Real-World Applications

- Validating user input that should read the same forwards/backwards (e.g. confirmation codes)
- In-place text buffer reversal in a text editor's undo/redo mechanism

---

## 💡 Core Pattern

### Template

```python
left = 0
right = len(values) - 1

while left < right:
    # Compare or swap
    left += 1
    right -= 1
```

### Pattern Recognition Clue
Palindrome, pair comparison, or processing from both ends.

---

## 🧠 Key Insights

1. Closing in from both ends halves the work compared to reversing then comparing — you stop the moment a mismatch is found.
2. Skipping non-alphanumeric characters with a `while` inside the outer `while` is the key trick for Valid Palindrome — it lets both pointers land only on characters that matter.
3. Reverse String is the simplest possible two-pointer swap — it's the template every other 'process from both ends' problem builds on.

---

## 📋 Practice Problems

### Problem 1: Valid Palindrome
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/valid-palindrome/

**Problem Statement:**
Given a string `s`, return `true` if it is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.

**Examples:**
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false

Input: s = " "
Output: true
```

**Constraints:**
- 1 <= s.length <= 2 * 10^5
- s consists of printable ASCII characters

**Solution Location:** [solutions/1_valid_palindrome.py](solutions/1_valid_palindrome.py)
**Practice Location:** [questions/valid_palindrome.py](questions/valid_palindrome.py)

**Approaches to Consider:**
- Brute force: filter into a cleaned string, compare to its reverse, O(n) time / O(n) space
- Optimized: two-pointer scan skipping non-alphanumeric chars, O(n) time / O(1) space
- Edge case: string with only punctuation/spaces

### Problem 2: Reverse String
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/reverse-string/

**Problem Statement:**
Write a function that reverses a string. The input string is given as an array of characters `s`, and it must be modified in-place with O(1) extra memory.

**Examples:**
```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

**Constraints:**
- 1 <= s.length <= 10^5
- s[i] is a printable ASCII character

**Solution Location:** [solutions/2_reverse_string.py](solutions/2_reverse_string.py)
**Practice Location:** [questions/reverse_string.py](questions/reverse_string.py)

**Approaches to Consider:**
- Brute force: use slicing/`reversed()` into a new list, O(n) extra space
- Optimized: two-pointer in-place swap, O(1) extra space
- Edge case: single-character array

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Valid Palindrome)
- [ ] Solve Problem 2 (Reverse String)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- Two pointers from opposite ends solve palindrome/reversal problems in O(n) time and O(1) space.
- Filtering logic (skip non-alphanumeric, normalize case) can live inside the same pointer loop — no separate cleaning pass needed.
- Comparing from both ends can short-circuit early, unlike building a reversed copy first.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 07](../Day-07/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

# Day 04: Strings and Frequency Maps

## 🎯 Learning Objectives

- Understand String traversal
- Understand Character counting
- Understand `collections.Counter`

---

## 📚 Concept: Strings and Frequency Maps

### Key Ideas

- String traversal
- Character counting
- `collections.Counter`

### Real-World Applications

- Spell-checking / anagram-based word games
- Validating that a message only uses characters available from a limited alphabet (e.g. rate-limited API keys)

---

## 💡 Core Pattern

### Template

```python
from collections import Counter

frequency = Counter(text)
```

### Pattern Recognition Clue
The answer depends on how many times each character or value appears.

---

## 🧠 Key Insights

1. `Counter` is a dict subclass — comparing two Counters with `==` checks that every key has the same count, which is exactly what an anagram check needs.
2. Subtracting one Counter from another (or checking `count[c] > available[c]`) tells you whether one multiset can be built from another.
3. Frequency-map problems are almost always O(n) — the trap is reaching for sorting (O(n log n)) when counting is enough.

---

## 📋 Practice Problems

### Problem 1: Valid Anagram
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/valid-anagram/

**Problem Statement:**
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. An anagram is a word formed by rearranging the letters of another, using all original letters exactly once.

**Examples:**
```
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
```

**Constraints:**
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters

**Solution Location:** [solutions/1_valid_anagram.py](solutions/1_valid_anagram.py)
**Practice Location:** [questions/valid_anagram.py](questions/valid_anagram.py)

**Approaches to Consider:**
- Brute force: sort both strings and compare, O(n log n)
- Optimized: compare character frequency counts, O(n)
- Edge case: different lengths (instant false)

### Problem 2: Ransom Note
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/ransom-note/

**Problem Statement:**
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine`, where each letter in `magazine` can only be used once.

**Examples:**
```
Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "ab"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
```

**Constraints:**
- 1 <= ransomNote.length, magazine.length <= 10^5
- ransomNote and magazine consist of lowercase English letters

**Solution Location:** [solutions/2_ransom_note.py](solutions/2_ransom_note.py)
**Practice Location:** [questions/ransom_note.py](questions/ransom_note.py)

**Approaches to Consider:**
- Brute force: remove each needed letter from a mutable copy of magazine, O(n^2)
- Optimized: compare frequency counts, O(n)
- Edge case: ransomNote longer than magazine

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (Valid Anagram)
- [ ] Solve Problem 2 (Ransom Note)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- Two strings are anagrams exactly when their character frequency maps are equal.
- 'Can A be built from B's letters' is a frequency-map subtraction/comparison, not a searching problem.
- Sorting solves frequency-shaped problems too, but counting is asymptotically better — reach for it first.

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 05](../Day-05/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

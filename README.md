# 🚀 30-Day DSA Mastery Plan — Python

> **Goal:** Build a strong foundation in Data Structures & Algorithms in 30 days with **1 hour of focused practice per day**, using **Python**.
> 
> **Primary focus:** Pattern recognition, interview problem solving, clean Python implementations, and time/space complexity.

---

## 📋 How to Use This Repository

### Daily 60-Minute Routine
- **10 min** — Learn: Understand today's concept and its time/space complexity
- **10 min** — Pattern: Write the core pattern/template from memory
- **35 min** — Solve: Solve 2 problems, ideally 1 Easy + 1 Medium
- **5 min** — Review: Record the pattern, key insight, mistake, and complexity

### Problem-Solving Framework

For every problem, follow this sequence:

1. **Understand** — What are the inputs, outputs, and constraints?
2. **Brute Force** — What is the simplest solution?
3. **Identify Pattern** — Which known DSA pattern applies?
4. **Optimize** — Can time or space complexity be improved?
5. **Code** — Write a clean Python solution
6. **Test** — Check normal cases and edge cases
7. **Analyze** — State time and space complexity

### The 20-Minute Rule

If you cannot solve a problem:
- Spend the first **10 minutes** trying independently
- Spend the next **5 minutes** writing the brute-force approach
- Spend the next **5 minutes** identifying the likely pattern
- Then look at a **hint**, not the full solution
- Re-solve the problem from scratch the next day

---

## 📅 30-Day Learning Path

### Week 1: Arrays, Hashing & Two Pointers
| Day | Topic | Status |
|-----|-------|--------|
| [Day 01](Day-01/README.md) | Big-O and Array Fundamentals | ⬜ |
| [Day 02](Day-02/README.md) | Hash Sets | ⬜ |
| [Day 03](Day-03/README.md) | Hash Maps | ⬜ |
| [Day 04](Day-04/README.md) | Strings and Frequency Maps | ⬜ |
| [Day 05](Day-05/README.md) | Two Pointers: Arrays | ⬜ |
| [Day 06](Day-06/README.md) | Two Pointers: Strings | ⬜ |
| [Day 07](Day-07/README.md) | Week 1 Revision | ⬜ |

### Week 2: Sliding Window, Prefix Sum, Binary Search & Linked Lists
| Day | Topic | Status |
|-----|-------|--------|
| [Day 08](Day-08/README.md) | Fixed Sliding Window | ⬜ |
| [Day 09](Day-09/README.md) | Variable Sliding Window | ⬜ |
| [Day 10](Day-10/README.md) | Prefix Sum | ⬜ |
| [Day 11](Day-11/README.md) | Binary Search | ⬜ |
| [Day 12](Day-12/README.md) | Modified Binary Search | ⬜ |
| [Day 13](Day-13/README.md) | Linked Lists | ⬜ |
| [Day 14](Day-14/README.md) | Fast & Slow Pointers | ⬜ |
| [Day 15](Day-15/README.md) | Midpoint Revision | ⬜ |

### Week 3: Stack, Queue & Trees
| Day | Topic | Status |
|-----|-------|--------|
| [Day 16](Day-16/README.md) | Stack | ⬜ |
| [Day 17](Day-17/README.md) | Monotonic Stack | ⬜ |
| [Day 18](Day-18/README.md) | Queue and BFS Foundations | ⬜ |
| [Day 19](Day-19/README.md) | Trees and DFS | ⬜ |
| [Day 20](Day-20/README.md) | Tree BFS | ⬜ |
| [Day 21](Day-21/README.md) | Binary Search Trees | ⬜ |
| [Day 22](Day-22/README.md) | Recursive Tree Problems | ⬜ |

### Week 4: Heap, Intervals, Graphs, Backtracking & DP
| Day | Topic | Status |
|-----|-------|--------|
| [Day 23](Day-23/README.md) | Heap / Priority Queue | ⬜ |
| [Day 24](Day-24/README.md) | Intervals | ⬜ |
| [Day 25](Day-25/README.md) | Graph DFS | ⬜ |
| [Day 26](Day-26/README.md) | Graph BFS | ⬜ |
| [Day 27](Day-27/README.md) | Backtracking | ⬜ |
| [Day 28](Day-28/README.md) | 1D Dynamic Programming | ⬜ |
| [Day 29](Day-29/README.md) | DP Practice | ⬜ |
| [Day 30](Day-30/README.md) | Final Pattern Recognition Challenge | ⬜ |

---

## 🎯 Pattern Recognition Cheat Sheet

| If the problem says... | Think... |
|------------------------|---------| 
| Duplicate / Exists / Frequency | Hash Set / Hash Map |
| Pair in sorted array | Two Pointers |
| Palindrome | Two Pointers |
| Contiguous subarray / substring | Sliding Window |
| Longest / shortest substring | Variable Sliding Window |
| Repeated range sum | Prefix Sum |
| Sorted array | Binary Search |
| Cycle / middle of linked list | Fast & Slow Pointers |
| Matching / nested brackets | Stack |
| Next greater / smaller | Monotonic Stack |
| Level by level | BFS |
| Shortest path, unweighted graph | BFS |
| Connected components | DFS / BFS |
| Top K / Kth largest | Heap |
| Overlapping ranges | Sort + Intervals |
| All combinations / permutations | Backtracking |
| Optimal answer from smaller answers | Dynamic Programming |

---

## 🛠️ Core Python DSA Toolkit

```python
# Hash Map
frequency = {}
frequency[x] = frequency.get(x, 0) + 1

# Hash Set
seen = set()
seen.add(x)

# Stack
stack = []
stack.append(x)
x = stack.pop()

# Queue
from collections import deque
queue = deque()
queue.append(x)
x = queue.popleft()

# Counter
from collections import Counter
counts = Counter(nums)

# Heap
import heapq
heapq.heappush(heap, x)
x = heapq.heappop(heap)

# Sorting
nums.sort()
sorted_nums = sorted(nums)
```

---

## 📊 Progress Tracker

| Week | Focus | Status |
|------|-------|--------|
| Week 1 | Arrays, Hashing, Two Pointers | ⬜ |
| Week 2 | Sliding Window, Prefix Sum, Binary Search, Linked Lists | ⬜ |
| Week 3 | Stack, Queue, Trees | ⬜ |
| Week 4 | Heap, Intervals, Graphs, Backtracking, DP | ⬜ |

**How to track:** Update the emoji in each day's folder when completed:
- ⬜ Not started
- 🟨 In progress
- ✅ Completed

---

## 📝 Repository Structure

```
dsa-mastery-30-days/
├── README.md                          # This file
├── PROGRESS.md                        # Overall progress tracker
├── MISTAKES_LOG.md                    # Common mistakes template
├── Day-01/
│   ├── README.md                      # Concept & pattern
│   ├── questions/
│   │   ├── 1_problem_name.md          # Problem statement
│   │   └── 2_problem_name.md
│   └── solutions/
│       ├── 1_solution.py              # Your solution
│       └── 2_solution.py
├── Day-02/
│   ├── README.md
│   ├── questions/
│   └── solutions/
└── ... (Day-03 through Day-30)
```

---

## 🎓 Target Outcome

By the end of this plan, aim to be able to:

- ✅ Recognize the likely DSA pattern before coding
- ✅ Explain brute-force and optimized approaches
- ✅ Write common Python DSA templates from memory
- ✅ Analyze time and space complexity
- ✅ Solve most Easy problems confidently
- ✅ Approach common Medium interview problems systematically

> **Remember:** Do not memorize 100 solutions. Master 10–15 reusable patterns.

---

## 📚 After 30 Days

Do not immediately jump to advanced algorithms. Spend another 2–4 weeks reinforcing the core patterns:

1. Solve **2–3 Medium problems per day**
2. Re-solve failed problems without looking at solutions
3. Practice identifying the pattern within **5 minutes**
4. Start timed sets of **2 problems in 45 minutes**
5. Add advanced topics gradually:
   - Trie
   - Union Find
   - Topological Sort
   - Dijkstra's Algorithm
   - Advanced Graphs
   - 2D Dynamic Programming
   - Greedy Algorithms
   - Bit Manipulation

---

## 📖 Resources

- **LeetCode:** https://leetcode.com
- **GeeksforGeeks:** https://www.geeksforgeeks.org
- **NeetCode:** https://neetcode.io
- **AlgoExpert:** https://www.algoexpert.io

---

## ✨ Let's Master DSA in 30 Days!

Start with **[Day 01](Day-01/README.md)** and commit to the 60-minute daily routine. Track your progress and celebrate every milestone! 🎉

---

*Last Updated: 2026-07-19*

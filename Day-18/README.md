# Day 18: Queue and BFS Foundations

## 🎯 Learning Objectives

- Understand FIFO principle
- Understand `collections.deque`
- Understand Level-by-level processing

---

## 📚 Concept: Queue and BFS Foundations

### Key Ideas

- FIFO principle
- `collections.deque`
- Level-by-level processing

### Real-World Applications

- Finding the shortest number of hops between two users in a social network
- Task/job scheduling where jobs are processed in the order they arrive

---

## 💡 Core Pattern

### Template

```python
from collections import deque

queue = deque([start])

while queue:
    node = queue.popleft()

    for neighbor in get_neighbors(node):
        queue.append(neighbor)
```

### Pattern Recognition Clue
Level-by-level exploration or shortest path.

---

## 🧠 Key Insights

1. A `deque` gives O(1) `popleft()`, unlike a plain list where `pop(0)` is O(n) — always use `deque` for BFS queues.
2. Marking a node visited *when you enqueue it* (not when you dequeue it) avoids adding the same node to the queue multiple times before it's ever processed.
3. BFS explores in increasing distance from the start, which is exactly why it finds the shortest path in an unweighted graph — the first time you reach a node is via the shortest route.

---

## 📋 Practice Problems

### Problem 1: BFS Template Implementation
**Difficulty:** Easy
**LeetCode:** (template exercise, not a single LeetCode problem)

**Problem Statement:**
Given a graph represented as an adjacency list (a dict mapping each node to a list of its neighbors) and a `start` node, return a list of nodes in the order they are visited by a breadth-first search.

**Examples:**
```
Input: graph = {'A': ['B','C'], 'B': ['D'], 'C': ['D'], 'D': []}, start = 'A'
Output: ['A', 'B', 'C', 'D']
```

**Constraints:**
- Graph has at most 1000 nodes
- Graph may be cyclic
- All node labels are hashable

**Solution Location:** [solutions/1_bfs_template.py](solutions/1_bfs_template.py)
**Practice Location:** [questions/bfs_template.py](questions/bfs_template.py)

**Approaches to Consider:**
- Naive: list-based queue using pop(0), O(n^2) due to repeated O(n) pops
- Optimized: deque-based queue with a visited set, O(V + E)
- Edge case: disconnected graph or start node with no neighbors

### Problem 2: Find if Path Exists in Graph
**Difficulty:** Easy
**LeetCode:** https://leetcode.com/problems/find-if-path-exists-in-graph/

**Problem Statement:**
There is a bi-directional graph with `n` vertices, labeled from `0` to `n - 1`. Given an array of `edges`, and two nodes `source` and `destination`, determine whether there is a valid path from `source` to `destination`.

**Examples:**
```
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
```

**Constraints:**
- 1 <= n <= 2 * 10^5
- 0 <= edges.length <= 2 * 10^5
- No self-loops or repeated edges

**Solution Location:** [solutions/2_bfs_graph.py](solutions/2_bfs_graph.py)
**Practice Location:** [questions/bfs_graph.py](questions/bfs_graph.py)

**Approaches to Consider:**
- Naive: unbounded DFS recursion without visited tracking (risks infinite loop on cycles)
- Optimized: BFS with adjacency list + visited set, O(V + E)
- Edge case: source equals destination

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1 (BFS Template Implementation)
- [ ] Solve Problem 2 (Find if Path Exists in Graph)
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- BFS with a `deque` explores a graph level by level and finds shortest paths in unweighted graphs.
- Mark nodes visited at enqueue time to avoid duplicate work, not at dequeue time.
- This queue+visited-set template is the foundation for every graph BFS problem in the coming days (grids, trees, multi-source BFS).

---

## 🎬 Next Steps

Once you complete this day:
1. Try each problem in `questions/` on your own first (no peeking!)
2. Compare against `solutions/` and study the optimized approach
3. Check edge cases
4. Verify complexity analysis
5. Move to [Day 19](../Day-19/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*

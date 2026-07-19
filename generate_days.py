#!/usr/bin/env python3
"""
Generate all Day-xx/README.md files based on the DSA plan
"""

from pathlib import Path

DAYS_DATA = [
    {
        "day": 2,
        "title": "Hash Sets",
        "concepts": [
            "Python `set` - O(1) average lookup",
            "Eliminating repeated searches",
            "Membership testing"
        ],
        "pattern": """```python
seen = set()

for num in nums:
    if num in seen:
        return True
    seen.add(num)

return False
```""",
        "recognition": "You need fast existence or duplicate checking.",
        "problems": [
            ("1_contains_duplicate.py", "Contains Duplicate", "Easy"),
            ("2_missing_number.py", "Missing Number", "Easy")
        ]
    },
    {
        "day": 3,
        "title": "Hash Maps",
        "concepts": [
            "Python dictionaries - Key-value lookup",
            "Complement technique",
            "Frequency counting"
        ],
        "pattern": """```python
seen = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in seen:
        return [seen[complement], i]

    seen[num] = i
```""",
        "recognition": "Storing previously seen information can eliminate a nested loop.",
        "problems": [
            ("1_two_sum.py", "Two Sum", "Easy"),
            ("2_majority_element.py", "Majority Element", "Easy")
        ]
    },
    {
        "day": 4,
        "title": "Strings and Frequency Maps",
        "concepts": [
            "String traversal",
            "Character counting",
            "`collections.Counter`"
        ],
        "pattern": """```python
from collections import Counter

frequency = Counter(text)
```""",
        "recognition": "The answer depends on how many times each character or value appears.",
        "problems": [
            ("1_valid_anagram.py", "Valid Anagram", "Easy"),
            ("2_ransom_note.py", "Ransom Note", "Easy")
        ]
    },
    {
        "day": 5,
        "title": "Two Pointers: Arrays",
        "concepts": [
            "Left/right pointers",
            "In-place array manipulation",
            "Sorted array optimization"
        ],
        "pattern": """```python
left = 0

for right in range(len(nums)):
    if condition:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
```""",
        "recognition": "You need to process an array using two positions without extra nested loops.",
        "problems": [
            ("1_move_zeroes.py", "Move Zeroes", "Easy"),
            ("2_remove_duplicates.py", "Remove Duplicates from Sorted Array", "Easy")
        ]
    },
    {
        "day": 6,
        "title": "Two Pointers: Strings",
        "concepts": [
            "Palindrome checking",
            "Two-pointer from both ends",
            "String manipulation"
        ],
        "pattern": """```python
left = 0
right = len(values) - 1

while left < right:
    # Compare or swap
    left += 1
    right -= 1
```""",
        "recognition": "Palindrome, pair comparison, or processing from both ends.",
        "problems": [
            ("1_valid_palindrome.py", "Valid Palindrome", "Easy"),
            ("2_reverse_string.py", "Reverse String", "Easy")
        ]
    },
    {
        "day": 7,
        "title": "Week 1 Revision",
        "concepts": [
            "Arrays",
            "Hash Set",
            "Hash Map",
            "Frequency counting",
            "Two Pointers"
        ],
        "pattern": """Challenge: Pick 3 unseen Easy/Medium problems.

For each problem, write:
```
Brute Force:
Pattern:
Optimized Approach:
Time Complexity:
Space Complexity:
```""",
        "recognition": "Mixed problems - identify pattern before solving!",
        "problems": [
            ("1_mixed_problem.py", "Mixed Problem 1", "Medium"),
            ("2_mixed_problem.py", "Mixed Problem 2", "Medium"),
            ("3_mixed_problem.py", "Mixed Problem 3", "Medium")
        ]
    },
    # Week 2
    {
        "day": 8,
        "title": "Fixed Sliding Window",
        "concepts": [
            "Fixed-size window",
            "Sliding mechanism",
            "Sum optimization"
        ],
        "pattern": """```python
window_sum = sum(nums[:k])
best = window_sum

for right in range(k, len(nums)):
    window_sum += nums[right]
    window_sum -= nums[right - k]
    best = max(best, window_sum)
```""",
        "recognition": "A fixed-size contiguous subarray or substring.",
        "problems": [
            ("1_max_avg_subarray.py", "Maximum Average Subarray I", "Easy"),
            ("2_max_sum_subarray.py", "Maximum Sum Subarray of Size K", "Easy")
        ]
    },
    {
        "day": 9,
        "title": "Variable Sliding Window",
        "concepts": [
            "Dynamic window size",
            "Expand/shrink logic",
            "Valid window conditions"
        ],
        "pattern": """```python
left = 0

for right in range(len(nums)):
    # Add right element

    while window_is_invalid:
        # Remove left element
        left += 1

    # Update answer
```""",
        "recognition": "Longest/shortest valid contiguous substring or subarray.",
        "problems": [
            ("1_longest_substring.py", "Longest Substring Without Repeating Characters", "Medium"),
            ("2_character_replacement.py", "Longest Repeating Character Replacement", "Medium")
        ]
    },
    {
        "day": 10,
        "title": "Prefix Sum",
        "concepts": [
            "Prefix sum array",
            "Range sum queries",
            "Cumulative calculations"
        ],
        "pattern": """```python
prefix = [0]

for num in nums:
    prefix.append(prefix[-1] + num)

range_sum = prefix[right + 1] - prefix[left]
```""",
        "recognition": "Repeated range sums or cumulative calculations.",
        "problems": [
            ("1_range_sum_query.py", "Range Sum Query - Immutable", "Easy"),
            ("2_subarray_sum_k.py", "Subarray Sum Equals K", "Medium")
        ]
    },
    {
        "day": 11,
        "title": "Binary Search",
        "concepts": [
            "Sorted array assumption",
            "Half-space elimination",
            "Mid calculation"
        ],
        "pattern": """```python
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
```""",
        "recognition": "Sorted input or the ability to eliminate half the search space.",
        "problems": [
            ("1_binary_search.py", "Binary Search", "Easy"),
            ("2_search_insert_pos.py", "Search Insert Position", "Easy")
        ]
    },
    {
        "day": 12,
        "title": "Modified Binary Search",
        "concepts": [
            "Rotated sorted arrays",
            "Finding pivot",
            "Conditional space elimination"
        ],
        "pattern": """```python
# Determine which half is sorted
# Decide which half contains target
# Adjust search boundaries accordingly
```""",
        "recognition": "Sorted array with a twist or unknown pivot point.",
        "problems": [
            ("1_search_rotated.py", "Search in Rotated Sorted Array", "Medium"),
            ("2_min_rotated.py", "Find Minimum in Rotated Sorted Array", "Medium")
        ]
    },
    {
        "day": 13,
        "title": "Linked Lists",
        "concepts": [
            "Node structure",
            "Pointer manipulation",
            "List reversal"
        ],
        "pattern": """```python
prev = None
current = head

while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node

return prev
```""",
        "recognition": "Node connections need to be changed without random access.",
        "problems": [
            ("1_reverse_list.py", "Reverse Linked List", "Easy"),
            ("2_merge_lists.py", "Merge Two Sorted Lists", "Easy")
        ]
    },
    {
        "day": 14,
        "title": "Fast & Slow Pointers",
        "concepts": [
            "Floyd's algorithm",
            "Cycle detection",
            "Middle finding"
        ],
        "pattern": """```python
slow = fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```""",
        "recognition": "Cycle detection or finding the middle of a linked structure.",
        "problems": [
            ("1_linked_cycle.py", "Linked List Cycle", "Easy"),
            ("2_middle_list.py", "Middle of the Linked List", "Easy")
        ]
    },
    {
        "day": 15,
        "title": "Midpoint Revision",
        "concepts": [
            "All patterns learned so far",
            "Timed problem solving",
            "Pattern recognition under pressure"
        ],
        "pattern": """Timed Challenge:
- 1 Easy: 10 minutes
- 1 Medium: 20 minutes
- 1 Medium: 25 minutes
- 5 minutes review""",
        "recognition": "Mixed problems - identify pattern before coding!",
        "problems": [
            ("1_timed_easy.py", "Timed Easy Problem", "Easy"),
            ("2_timed_medium_1.py", "Timed Medium Problem 1", "Medium"),
            ("3_timed_medium_2.py", "Timed Medium Problem 2", "Medium")
        ]
    },
    # Week 3
    {
        "day": 16,
        "title": "Stack",
        "concepts": [
            "LIFO principle",
            "Matching brackets",
            "Undo operations"
        ],
        "pattern": """```python
stack = []

for item in items:
    if should_push:
        stack.append(item)
    else:
        top = stack.pop()
```""",
        "recognition": "Matching, nested structures, undo operations, or LIFO behavior.",
        "problems": [
            ("1_valid_parentheses.py", "Valid Parentheses", "Easy"),
            ("2_min_stack.py", "Min Stack", "Medium")
        ]
    },
    {
        "day": 17,
        "title": "Monotonic Stack",
        "concepts": [
            "Ordered element storage",
            "Next greater element",
            "O(n) solution for O(n²) problem"
        ],
        "pattern": """```python
stack = []

for i, value in enumerate(nums):
    while stack and nums[stack[-1]] < value:
        index = stack.pop()
        # Process answer for index

    stack.append(i)
```""",
        "recognition": "Next greater/smaller element.",
        "problems": [
            ("1_daily_temps.py", "Daily Temperatures", "Medium"),
            ("2_next_greater.py", "Next Greater Element I", "Easy")
        ]
    },
    {
        "day": 18,
        "title": "Queue and BFS Foundations",
        "concepts": [
            "FIFO principle",
            "`collections.deque`",
            "Level-by-level processing"
        ],
        "pattern": """```python
from collections import deque

queue = deque([start])

while queue:
    node = queue.popleft()

    for neighbor in get_neighbors(node):
        queue.append(neighbor)
```""",
        "recognition": "Level-by-level exploration or shortest path.",
        "problems": [
            ("1_bfs_template.py", "BFS Template Implementation", "Easy"),
            ("2_bfs_graph.py", "Simple BFS Graph Problem", "Medium")
        ]
    },
    {
        "day": 19,
        "title": "Trees and DFS",
        "concepts": [
            "Recursive traversal",
            "Base cases",
            "Subtree processing"
        ],
        "pattern": """```python
def dfs(node):
    if not node:
        return

    dfs(node.left)
    dfs(node.right)
```""",
        "recognition": "Fully explore branches or recursively process subtrees.",
        "problems": [
            ("1_max_depth.py", "Maximum Depth of Binary Tree", "Easy"),
            ("2_same_tree.py", "Same Tree", "Easy")
        ]
    },
    {
        "day": 20,
        "title": "Tree BFS",
        "concepts": [
            "Level-order traversal",
            "Level-size tracking",
            "Deque usage"
        ],
        "pattern": """```python
# Use deque for level-order traversal
# Process all nodes at current level
# Move to next level
```""",
        "recognition": "Level-by-level tree processing.",
        "problems": [
            ("1_level_order.py", "Binary Tree Level Order Traversal", "Medium"),
            ("2_avg_levels.py", "Average of Levels in Binary Tree", "Medium")
        ]
    },
    {
        "day": 21,
        "title": "Binary Search Trees",
        "concepts": [
            "BST properties",
            "Left < node < Right",
            "Recursive validation"
        ],
        "pattern": """```python
# Verify: left subtree < node
# Verify: right subtree > node
# Recursively check bounds
```""",
        "recognition": "Search efficiency or BST property validation.",
        "problems": [
            ("1_search_bst.py", "Search in a Binary Search Tree", "Easy"),
            ("2_validate_bst.py", "Validate Binary Search Tree", "Medium")
        ]
    },
    {
        "day": 22,
        "title": "Recursive Tree Problems",
        "concepts": [
            "Subproblem decomposition",
            "Left/right subtree answers",
            "Combining results"
        ],
        "pattern": """```python
# Solve for left subtree
# Solve for right subtree
# Combine answers
# Return or update global
```""",
        "recognition": "Tree problem requiring answers from both subtrees.",
        "problems": [
            ("1_invert_tree.py", "Invert Binary Tree", "Easy"),
            ("2_diameter_tree.py", "Diameter of Binary Tree", "Medium")
        ]
    },
    # Week 4
    {
        "day": 23,
        "title": "Heap / Priority Queue",
        "concepts": [
            "Min-heap (Python default)",
            "Heapify operations",
            "K-smallest/largest problems"
        ],
        "pattern": """```python
import heapq

heap = []

for value in nums:
    heapq.heappush(heap, value)

    if len(heap) > k:
        heapq.heappop(heap)
```""",
        "recognition": "Top K, Kth largest/smallest, or repeatedly selecting min/max.",
        "problems": [
            ("1_kth_largest.py", "Kth Largest Element in an Array", "Medium"),
            ("2_top_k_frequent.py", "Top K Frequent Elements", "Medium")
        ]
    },
    {
        "day": 24,
        "title": "Intervals",
        "concepts": [
            "Overlapping detection",
            "Interval merging",
            "Sort by start point"
        ],
        "pattern": """```python
intervals.sort(key=lambda x: x[0])
merged = []

for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])
```""",
        "recognition": "Overlapping ranges, meetings, schedules, start/end times.",
        "problems": [
            ("1_merge_intervals.py", "Merge Intervals", "Medium"),
            ("2_insert_interval.py", "Insert Interval", "Medium")
        ]
    },
    {
        "day": 25,
        "title": "Graph DFS",
        "concepts": [
            "Connected components",
            "Graph traversal",
            "Visited tracking"
        ],
        "pattern": """```python
def dfs(row, col):
    if invalid_or_visited:
        return

    mark_visited(row, col)

    for next_row, next_col in neighbors:
        dfs(next_row, next_col)
```""",
        "recognition": "Connected components or exploring all connected nodes.",
        "problems": [
            ("1_number_islands.py", "Number of Islands", "Medium"),
            ("2_max_area_island.py", "Max Area of Island", "Medium")
        ]
    },
    {
        "day": 26,
        "title": "Graph BFS",
        "concepts": [
            "Queue-based traversal",
            "Shortest path",
            "Multi-source BFS"
        ],
        "pattern": """```python
# Use queue for exploration
# Track visited nodes
# Process level by level
```""",
        "recognition": "Shortest path in unweighted graph or level-by-level exploration.",
        "problems": [
            ("1_flood_fill.py", "Flood Fill", "Medium"),
            ("2_rotting_oranges.py", "Rotting Oranges", "Medium")
        ]
    },
    {
        "day": 27,
        "title": "Backtracking",
        "concepts": [
            "Choose → Explore → Undo",
            "Decision tree",
            "All possibilities"
        ],
        "pattern": """```python
result = []

def backtrack(path, choices):
    if goal_reached:
        result.append(path.copy())
        return

    for choice in choices:
        path.append(choice)
        backtrack(path, new_choices)
        path.pop()
```

Remember: **Choose → Explore → Undo**""",
        "recognition": "Generate all combinations, permutations, subsets, or possible configurations.",
        "problems": [
            ("1_subsets.py", "Subsets", "Medium"),
            ("2_permutations.py", "Permutations", "Medium")
        ]
    },
    {
        "day": 28,
        "title": "1D Dynamic Programming",
        "concepts": [
            "State definition",
            "Recurrence relation",
            "Base cases"
        ],
        "pattern": """```python
dp = [0] * (n + 1)

dp[0] = base_case

for i in range(1, n + 1):
    dp[i] = transition_from_previous_states
```""",
        "recognition": "The current answer depends on previously solved smaller problems.",
        "problems": [
            ("1_climbing_stairs.py", "Climbing Stairs", "Easy"),
            ("2_house_robber.py", "House Robber", "Medium")
        ]
    },
    {
        "day": 29,
        "title": "Dynamic Programming Practice",
        "concepts": [
            "State identification",
            "Recurrence construction",
            "Optimization techniques"
        ],
        "pattern": """For every DP problem answer:
1. What is the state?
2. What is the recurrence?
3. What are the base cases?
4. In what order should states be calculated?
5. Can space be optimized?""",
        "recognition": "Optimization problem with optimal substructure.",
        "problems": [
            ("1_coin_change.py", "Coin Change", "Medium"),
            ("2_decode_ways.py", "Decode Ways or Min Cost Climbing Stairs", "Medium")
        ]
    },
    {
        "day": 30,
        "title": "Final Pattern Recognition Challenge",
        "concepts": [
            "All 15 core patterns",
            "Mixed problem solving",
            "Speed and accuracy"
        ],
        "pattern": """Before coding each problem, write:
```
Input:
Output:
Constraints:
Brute Force:
Pattern:
Why this pattern:
Time Complexity:
Space Complexity:
```

Suggested mix:
- 1 Array/Hashing problem
- 1 Sliding Window/Two Pointer problem
- 1 Tree/Graph problem
- 1 Heap/Interval problem
- 1 DP/Backtracking problem""",
        "recognition": "No hints - identify pattern from problem alone!",
        "problems": [
            ("1_challenge_1.py", "Challenge Problem 1", "Mixed"),
            ("2_challenge_2.py", "Challenge Problem 2", "Mixed"),
            ("3_challenge_3.py", "Challenge Problem 3", "Mixed"),
            ("4_challenge_4.py", "Challenge Problem 4", "Mixed"),
            ("5_challenge_5.py", "Challenge Problem 5", "Mixed")
        ]
    }
]


def generate_day_readme(day_num, data):
    """Generate README content for a single day"""

    problems_section = "\n\n".join([
        f"""### Problem {i+1}: {prob[1]}
**Difficulty:** {prob[2]}

**Problem Statement:**
[Add problem statement here from LeetCode or problem source]

**Examples:**
[Add examples here]

**Constraints:**
[Add constraints here]

**Solution Location:** [solutions/{prob[0]}](solutions/{prob[0]})

**Approaches to Consider:**
- Brute force solution
- Optimized approach
- Edge cases and validation"""
        for i, prob in enumerate(data["problems"])
    ])

    content = f"""# Day {day_num:02d}: {data['title']}

## 🎯 Learning Objectives

- {chr(10).join([f"Understand {c}" for c in data['concepts']])}

---

## 📚 Concept: {data['title']}

### Key Ideas

{chr(10).join([f"- {c}" for c in data['concepts']])}

### Real-World Applications

- [Add real-world use cases]
- [Add more examples]

---

## 💡 Core Pattern

### Template

{data['pattern']}

### Pattern Recognition Clue
{data['recognition']}

---

## 🧠 Key Insights

1. [Key insight 1]
2. [Key insight 2]
3. [Key insight 3]

---

## 📋 Practice Problems

{problems_section}

---

## ✅ Daily Checklist

- [ ] Understand the concept
- [ ] Write the pattern from memory
- [ ] Solve Problem 1
- [ ] Solve Problem 2
- [ ] Explain complexity analysis
- [ ] Record insights in mistakes log if needed

---

## 📝 Key Takeaways

- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]

---

## 🎬 Next Steps

Once you complete this day:
1. Review your solutions
2. Check edge cases
3. Verify complexity analysis
4. Move to [Day {day_num+1:02d}](../Day-{day_num+1:02d}/README.md)

**Time Goal:** 60 minutes
- Learn: 10 min
- Pattern: 10 min
- Solve: 35 min
- Review: 5 min

---

*Track your progress: Update the main [README.md](../README.md) when completed!*
"""
    return content


# Generate all day READMEs
base_path = Path(__file__).parent

for day_data in DAYS_DATA:
    day_num = day_data["day"]
    day_folder = base_path / f"Day-{day_num:02d}"
    readme_path = day_folder / "README.md"

    # Create README
    content = generate_day_readme(day_num, day_data)
    readme_path.write_text(content)

    # Create empty solution files
    solutions_folder = day_folder / "solutions"
    solutions_folder.mkdir(exist_ok=True)

    for prob_filename, prob_title, difficulty in day_data["problems"]:
        solution_path = solutions_folder / prob_filename
        solution_content = f'''"""
Problem: {prob_title}
Difficulty: {difficulty}

[Add problem statement and examples]
"""

# TODO: Implement solution

if __name__ == "__main__":
    # Test cases
    pass
'''
        solution_path.write_text(solution_content)

    print(f"✅ Generated Day {day_num:02d}: {day_data['title']}")

print("\n🎉 All days generated successfully!")

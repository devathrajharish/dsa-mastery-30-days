"""
Problem: BFS Template Implementation
Difficulty: Easy

Given a graph as an adjacency list and a start node, return the nodes
in breadth-first-search visit order.
"""

from collections import deque


def bfs_list_queue(graph, start):
    """
    Naive - Use a plain list as the queue.
    Time: O(V^2) - list.pop(0) is O(V), done V times
    Space: O(V)
    """
    visited = {start}
    order = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def bfs_deque_queue(graph, start):
    """
    Optimized - Use collections.deque for O(1) popleft.
    Time: O(V + E)
    Space: O(V)

    Key Insight: Mark a node visited the moment it's enqueued, not when
    it's dequeued, to avoid enqueuing duplicates.
    """
    visited = {start}
    order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    expected = ["A", "B", "C", "D"]

    result = bfs_deque_queue(graph, "A")
    status = "✅" if result == expected else "❌"
    print(f"{status} BFS from 'A' -> {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Naive:     Time O(V^2), Space O(V)")
    print("Optimized: Time O(V+E), Space O(V)")

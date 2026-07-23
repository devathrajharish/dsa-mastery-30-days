"""
Problem: Find if Path Exists in Graph
Difficulty: Easy
LeetCode: https://leetcode.com/problems/find-if-path-exists-in-graph/

Given an undirected graph, determine if a path exists between source
and destination.
"""

from collections import defaultdict, deque
from typing import List


def valid_path_dfs(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    Alternative - Recursive DFS with visited tracking.
    Time: O(V + E)
    Space: O(V + E)
    """
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()

    def dfs(node):
        if node == destination:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited and dfs(neighbor):
                return True
        return False

    return dfs(source)


def valid_path_bfs(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    """
    Optimized - BFS with adjacency list and visited set.
    Time: O(V + E)
    Space: O(V + E)
    """
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = {source}
    queue = deque([source])

    while queue:
        node = queue.popleft()
        if node == destination:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False


if __name__ == "__main__":
    test_cases = [
        (3, [[0, 1], [1, 2], [2, 0]], 0, 2, True),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5, False),
    ]

    for n, edges, source, dest, expected in test_cases:
        result = valid_path_bfs(n, edges, source, dest)
        status = "✅" if result == expected else "❌"
        print(f"{status} n={n}, source={source}, dest={dest} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("DFS: Time O(V+E), Space O(V+E)")
    print("BFS: Time O(V+E), Space O(V+E)")

"""
Problem: BFS Template Implementation
Difficulty: Easy

Given a graph as an adjacency list and a start node, return the nodes
in breadth-first-search visit order.
"""

from collections import deque


def bfs(graph, start):
    """
    Time: O(?)
    Space: O(?)
    """
    # TODO: implement your solution here
    pass


if __name__ == "__main__":
    graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
    print(bfs(graph, "A"))  # Expected: ['A', 'B', 'C', 'D']

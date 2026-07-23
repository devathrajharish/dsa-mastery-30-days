"""
Problem: Linked List Cycle
Difficulty: Easy
LeetCode: https://leetcode.com/problems/linked-list-cycle/

Determine if a linked list has a cycle.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle_bruteforce(head) -> bool:
    """
    Brute Force - Track visited nodes in a set.
    Time: O(n)
    Space: O(n)
    """
    seen = set()
    current = head
    while current:
        if current in seen:
            return True
        seen.add(current)
        current = current.next
    return False


def has_cycle_optimized(head) -> bool:
    """
    Optimized - Floyd's fast/slow pointer (tortoise and hare).
    Time: O(n)
    Space: O(1)

    Key Insight: If a cycle exists, the faster pointer will eventually
    lap the slower one inside the loop.
    """
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


def _build_list_with_cycle(values, pos):
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], -1, False),
    ]

    for values, pos, expected in test_cases:
        head = _build_list_with_cycle(values, pos)
        result = has_cycle_optimized(head)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {values}, pos={pos} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n), Space O(n)")
    print("Optimized:   Time O(n), Space O(1)")

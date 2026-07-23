"""
Problem: Reverse Linked List
Difficulty: Easy
LeetCode: https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse it and return the new
head.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    """Helper: build a linked list from a Python list."""
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def linked_list_to_list(head):
    """Helper: convert a linked list back to a Python list."""
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def reverse_list_iterative(head):
    """
    Iterative - Rewire each node's next pointer as we walk the list.
    Time: O(n)
    Space: O(1)
    """
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def reverse_list_recursive(head):
    """
    Recursive - Reverse everything after head, then point the next
    node's next back at head.
    Time: O(n)
    Space: O(n) - recursion call stack
    """
    if not head or not head.next:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([], []),
    ]

    for values, expected in test_cases:
        head = build_linked_list(values)
        reversed_head = reverse_list_iterative(head)
        result = linked_list_to_list(reversed_head)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {values} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Iterative: Time O(n), Space O(1)")
    print("Recursive: Time O(n), Space O(n)")

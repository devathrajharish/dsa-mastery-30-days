"""
Problem: Reverse Linked List
Difficulty: Easy

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


def reverse_list(head):
    """
    Time: O(?)
    Space: O(?)
    """
    # TODO: implement your solution here
    pass


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    print(linked_list_to_list(reverse_list(head)))  # Expected: [5, 4, 3, 2, 1]

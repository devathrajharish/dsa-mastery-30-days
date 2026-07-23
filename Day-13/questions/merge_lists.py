"""
Problem: Merge Two Sorted Lists
Difficulty: Easy

Merge two sorted linked lists into one sorted list by splicing nodes.
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


def merge_two_lists(list1, list2):
    """
    Time: O(?)
    Space: O(?)
    """
    # TODO: implement your solution here
    pass


if __name__ == "__main__":
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])
    print(linked_list_to_list(merge_two_lists(l1, l2)))  # Expected: [1, 1, 2, 3, 4]

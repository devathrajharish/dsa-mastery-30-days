"""
Problem: Linked List Cycle
Difficulty: Easy

Determine if a linked list has a cycle.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    """
    Time: O(?)
    Space: O(?)
    """
    # TODO: implement your solution here
    pass


if __name__ == "__main__":
    a = ListNode(3)
    b = ListNode(2)
    c = ListNode(0)
    d = ListNode(-4)
    a.next, b.next, c.next, d.next = b, c, d, b  # cycle back to b
    print(has_cycle(a))  # Expected: True

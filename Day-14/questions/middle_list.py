"""
Problem: Middle of the Linked List
Difficulty: Easy

Return the middle node of a singly linked list (second middle if two).
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next


def linked_list_to_list(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values


def middle_node(head):
    """
    Time: O(?)
    Space: O(?)
    """
    # TODO: implement your solution here
    pass


if __name__ == "__main__":
    head = build_linked_list([1, 2, 3, 4, 5])
    print(linked_list_to_list(middle_node(head)))  # Expected: [3, 4, 5]

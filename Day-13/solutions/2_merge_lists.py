"""
Problem: Merge Two Sorted Lists
Difficulty: Easy
LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/

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


def merge_two_lists_bruteforce(list1, list2):
    """
    Brute Force - Collect all values, sort, rebuild.
    Time: O((n+m) log(n+m))
    Space: O(n+m)
    """
    values = []
    for head in (list1, list2):
        while head:
            values.append(head.val)
            head = head.next
    values.sort()
    return build_linked_list(values)


def merge_two_lists_optimized(list1, list2):
    """
    Optimized - Iterative merge using a dummy node.
    Time: O(n + m)
    Space: O(1) - reuses existing nodes

    Key Insight: A dummy head avoids special-casing which list starts
    the result.
    """
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 else list2
    return dummy.next


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ]

    for v1, v2, expected in test_cases:
        l1 = build_linked_list(v1)
        l2 = build_linked_list(v2)
        merged = merge_two_lists_optimized(l1, l2)
        result = linked_list_to_list(merged)
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {v1}, {v2} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O((n+m) log(n+m)), Space O(n+m)")
    print("Optimized:   Time O(n+m),            Space O(1)")

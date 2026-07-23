"""
Problem: Middle of the Linked List
Difficulty: Easy
LeetCode: https://leetcode.com/problems/middle-of-the-linked-list/

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


def middle_node_bruteforce(head):
    """
    Brute Force - Count the length, then walk to the middle index.
    Time: O(n) - two passes
    Space: O(1)
    """
    length = 0
    node = head
    while node:
        length += 1
        node = node.next

    node = head
    for _ in range(length // 2):
        node = node.next
    return node


def middle_node_optimized(head):
    """
    Optimized - Fast/slow pointer, one pass.
    Time: O(n)
    Space: O(1)

    Key Insight: When fast reaches the end (moving 2 steps at a time),
    slow (moving 1 step at a time) is exactly at the middle.
    """
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
    ]

    for values, expected in test_cases:
        head = build_linked_list(values)
        result = linked_list_to_list(middle_node_optimized(head))
        status = "✅" if result == expected else "❌"
        print(f"{status} Input: {values} -> Output: {result} (Expected: {expected})")

    print("\n📊 Complexity Analysis:")
    print("Brute Force: Time O(n), Space O(1)")
    print("Optimized:   Time O(n), Space O(1)")

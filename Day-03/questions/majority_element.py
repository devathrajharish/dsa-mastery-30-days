"""
Problem: Majority Element
Difficulty: Easy

Given an array nums of size n, return the majority element (the one
that appears more than n / 2 times). Always exists.
"""


from itertools import count


def majority_element(nums):
    """
    Time: O(?)
    Space: O(?)
    """
    counts = {}
    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    return max(counts, key=counts.get)



if __name__ == "__main__":
    print(majority_element([3, 2, 3]))              # Expected: 3
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))   # Expected: 2

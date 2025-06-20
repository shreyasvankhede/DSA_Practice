"""
Problem: Merge Two Sorted Lists
LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/
Category: Linked List
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        # Initialize result and head pointers
        if list1.val < list2.val:
            result = list1
            list1 = list1.next
        else:
            result = list2
            list2 = list2.next

        head = result  # Head will track the start of the merged list

        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        # Append remaining elements
        if list1:
            head.next = list1
        if list2:
            head.next = list2

        return result


# Helper to create linked list from list
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper to convert linked list to list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    # Sample test case
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    sol = Solution()
    merged = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # Expected output: [1, 1, 2, 3, 4, 4]

"""
Problem: Add Two Numbers
LeetCode: https://leetcode.com/problems/add-two-numbers/
Category: Linked List
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        prev_carry = 0

        # Add nodes from both lists while both have elements
        while l1 and l2:
            val = l1.val + l2.val + prev_carry
            carry = val // 10
            rem = val % 10
            current.next = ListNode(rem)
            current = current.next
            prev_carry = carry
            l1 = l1.next
            l2 = l2.next

        # Add remaining nodes from l1
        while l1:
            val = l1.val + prev_carry
            carry = val // 10
            rem = val % 10
            current.next = ListNode(rem)
            current = current.next
            prev_carry = carry
            l1 = l1.next

        # Add remaining nodes from l2
        while l2:
            val = l2.val + prev_carry
            carry = val // 10
            rem = val % 10
            current.next = ListNode(rem)
            current = current.next
            prev_carry = carry
            l2 = l2.next

        # Add final carry if any
        if prev_carry:
            current.next = ListNode(prev_carry)

        return head.next


# Helper function to create a linked list from a list of integers
def create_linked_list(nums):
    dummy = ListNode()
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to print a linked list as a list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    # Sample test case
    l1 = create_linked_list([2, 4, 3])  # represents number 342
    l2 = create_linked_list([5, 6, 4])  # represents number 465
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print(linked_list_to_list(result))  # Expected output: [7, 0, 8], represents number 807

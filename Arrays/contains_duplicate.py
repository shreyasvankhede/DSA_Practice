"""
Problem: Contains Duplicate
LeetCode: https://leetcode.com/problems/contains-duplicate/
Category: Array, Hash Set
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Returns True if any value appears at least twice in the list.
        Uses a set to check for duplicates.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    # Sample test case
    nums = [1, 2, 3, 1]
    sol = Solution()
    print(sol.containsDuplicate(nums))  # Expected output: True

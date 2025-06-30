"""
Problem: Remove Element
LeetCode: https://leetcode.com/problems/remove-element/
Category: Array, Two Pointers
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j


if __name__ == "__main__":
    # Sample test case
    nums = [3, 2, 2, 3]
    val = 3
    sol = Solution()
    k = sol.removeElement(nums, val)
    print(k, nums[:k])  # Expected output: 2 [2, 2]

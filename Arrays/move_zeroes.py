"""
Problem: Move Zeroes
LeetCode: https://leetcode.com/problems/move-zeroes/
Category: Array, Two Pointers
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all 0s to the end while maintaining the order of non-zero elements.
        Modifies the input list in-place.
        """
        j = 0  # Position to place the next non-zero element

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


if __name__ == "__main__":
    # Sample test case
    nums = [0, 1, 0, 3, 12]
    sol = Solution()
    sol.moveZeroes(nums)
    print(nums)  # Expected output: [1, 3, 12, 0, 0]

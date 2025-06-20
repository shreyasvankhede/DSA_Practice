"""
Problem: Single Number
LeetCode: https://leetcode.com/problems/single-number/
Category: Array, Bit Manipulation
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        XOR all elements. Pairs cancel out, leaving the single number.
        """
        ans = nums[0]
        for i in nums[1:]:  # Exclude the first element already in ans
            ans = ans ^ i   # XOR operation
        return ans


if __name__ == "__main__":
    # Sample test case
    nums = [4, 1, 2, 1, 2]
    sol = Solution()
    print(sol.singleNumber(nums))  # Expected output: 4

"""
Problem: Concatenation of Array
LeetCode: https://leetcode.com/problems/concatenation-of-array/
Category: Array
"""

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


if __name__ == "__main__":
    # Sample test case
    nums = [1, 2, 1]
    sol = Solution()
    print(sol.getConcatenation(nums))  # Expected output: [1, 2, 1, 1, 2, 1]

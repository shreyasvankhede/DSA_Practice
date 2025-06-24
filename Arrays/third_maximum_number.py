"""
Problem: Third Maximum Number
LeetCode: https://leetcode.com/problems/third-maximum-number/
Category: Array, Sorting
Approach: Track top 3 unique max values in a single pass.
"""

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        Returns the third distinct maximum number in the list.
        If it does not exist, returns the maximum number.
        """
        INT_MIN = -2**31 - 1  # Lower than any 32-bit int
        h1 = h2 = h3 = INT_MIN

        for num in nums:
            if num == h1 or num == h2 or num == h3:
                continue
            if num > h1:
                h3, h2, h1 = h2, h1, num
            elif num > h2:
                h3, h2 = h2, num
            elif num > h3:
                h3 = num

        return h3 if h3 != INT_MIN else h1


if __name__ == "__main__":
    # Sample test case
    nums = [2, 2, 3, 1]
    sol = Solution()
    print(sol.thirdMax(nums))  # Expected output: 1

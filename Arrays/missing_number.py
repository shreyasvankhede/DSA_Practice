"""
Problem: Missing Number
LeetCode: https://leetcode.com/problems/missing-number/
Category: Array, Brute-force
Note: This is a brute-force O(n²) solution.
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Check each number from 0 to n and return the missing one.
        Brute-force approach with O(n²) time complexity.
        """
        n = len(nums)
        for i in range(n + 1):
            found = False
            for num in nums:
                if num == i:
                    found = True
                    break
            if not found:
                return i
        return 0


if __name__ == "__main__":
    # Sample test case
    nums = [3, 0, 1]
    sol = Solution()
    print(sol.missingNumber(nums))  # Expected output: 2

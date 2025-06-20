"""
Problem: Maximum Subarray
LeetCode: https://leetcode.com/problems/maximum-subarray/
Category: Array, Dynamic Programming (Kadane's Algorithm)
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Implements Kadane's Algorithm.
        Tracks the maximum sum of a contiguous subarray.
        """
        current_sum = 0
        max_sum = float('-inf')

        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            if current_sum < 0:
                current_sum = 0

        return max_sum


if __name__ == "__main__":
    # Sample test case
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    print(sol.maxSubArray(nums))  # Expected output: 6
    # Explanation: [4, -1, 2, 1] has the largest sum = 6

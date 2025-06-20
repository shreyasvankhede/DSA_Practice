"""
Problem: Max Consecutive Ones
LeetCode: https://leetcode.com/problems/max-consecutive-ones/
Category: Array
"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Counts the maximum number of consecutive 1s in the binary array.
        """
        max_count = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count


if __name__ == "__main__":
    # Sample test case
    nums = [1, 1, 0, 1, 1, 1]
    sol = Solution()
    print(sol.findMaxConsecutiveOnes(nums))  # Expected output: 3

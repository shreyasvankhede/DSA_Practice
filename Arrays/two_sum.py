"""
Problem: Two Sum
LeetCode: https://leetcode.com/problems/two-sum/
Category: Array, HashMap (Brute-force version)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute-force approach: check all pairs to find two numbers that sum to target.
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    # Sample test case
    nums = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))  # Expected output: [0, 1]

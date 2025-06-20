"""
Problem: Majority Element
LeetCode: https://leetcode.com/problems/majority-element/
Category: Array, Boyer-Moore Voting Algorithm
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore Voting Algorithm:
        The majority element appears more than n//2 times.
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate


if __name__ == "__main__":
    # Sample test case
    nums = [2, 2, 1, 1, 1, 2, 2]
    sol = Solution()
    print(sol.majorityElement(nums))  # Expected output: 2

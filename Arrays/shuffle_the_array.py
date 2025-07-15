"""
Problem: Shuffle the Array
LeetCode: https://leetcode.com/problems/shuffle-the-array/
Category: Array
"""

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        num = [0] * len(nums)
        j = n
        a = 0
        for i in range(n):
            num[a], num[a + 1] = nums[i], nums[j]
            j += 1
            a += 2
        return num


if __name__ == "__main__":
    # Sample test case
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    sol = Solution()
    print(sol.shuffle(nums, n))  # Expected output: [2, 3, 5, 4, 1, 7]

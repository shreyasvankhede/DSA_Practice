"""
Problem: Median of Two Sorted Arrays
LeetCode: https://leetcode.com/problems/median-of-two-sorted-arrays/
Category: Array, Binary Search (Note: this version uses merge + sort)
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Merges two arrays, sorts them, and returns the median.
        Time complexity: O((m+n) log(m+n))
        """
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)

        if n % 2 == 1:
            return float(nums[n // 2])
        else:
            return (nums[n // 2] + nums[(n // 2) - 1]) / 2


if __name__ == "__main__":
    # Sample test case
    nums1 = [1, 3]
    nums2 = [2]
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1, nums2))  # Expected output: 2.0

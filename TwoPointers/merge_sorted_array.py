"""
Problem: Merge Sorted Array
LeetCode: https://leetcode.com/problems/merge-sorted-array/
Category: Array, Two Pointers
Note: This version uses a simple bubble sort after merging. Not optimal for large inputs.
There is an inbuilt sort function it python but it wont teach me anything about algorithms,but it wouldve resulted into a better time complexity
"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges nums2 into nums1 in-place. Assumes nums1 has enough space (length m + n).
        Uses simple sorting after placing nums2 elements — time complexity is O((m+n)^2).
        """
        # Copy elements from nums2 into nums1
        for i in range(n):
            nums1[m + i] = nums2[i]

        # Sort the combined array using bubble sort
        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                if nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]


if __name__ == "__main__":
    # Sample test case
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
    print(nums1)  # Expected output: [1, 2, 2, 3, 5, 6]

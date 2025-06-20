"""
Problem: Remove Duplicates from Sorted Array
LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Category: Array, Two Pointers
Note: This version uses extra space, not fully in-place as required by LeetCode.
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array and returns the length of the unique part.
        This version creates a new list and then reassigns it.
        """
        unique_nums = []
        prev = float('-inf')

        for num in nums:
            if num != prev:
                unique_nums.append(num)
                prev = num

        # Copy back into original array
        for i in range(len(unique_nums)):
            nums[i] = unique_nums[i]

        return len(unique_nums)


if __name__ == "__main__":
    # Sample test case
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    sol = Solution()
    k = sol.removeDuplicates(nums)
    print(k)            # Expected output: 5
    print(nums[:k])     # Expected output: [0, 1, 2]()

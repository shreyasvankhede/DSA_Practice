"""
Problem: Sort Colors
LeetCode: https://leetcode.com/problems/sort-colors/
Category: Array, Sorting
Note: This is a bubble sort approach (O(n²)), not the optimal solution.
"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts the list in-place using bubble sort.
        Only works well for small inputs. Time complexity: O(n²).
        """
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
    # Sample test case
    nums = [2, 0, 2, 1, 1, 0]
    sol = Solution()
    sol.sortColors(nums)
    print(nums)  # Expected output: [0, 0, 1, 1, 2, 2]

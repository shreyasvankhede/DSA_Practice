"""
Problem: Container With Most Water
LeetCode: https://leetcode.com/problems/container-with-most-water/
Category: Two Pointers, Array
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        while i < j:
            wall = min(height[i], height[j])
            dist = j - i
            area = wall * dist
            max_area = max(max_area, area)
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return max_area


if __name__ == "__main__":
    # Sample test case
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    sol = Solution()
    print(sol.maxArea(height))  # Expected output: 49

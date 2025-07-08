"""
Problem: Find the Index of the First Occurrence in a String
LeetCode: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
Category: String
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ind = haystack.find(needle)
        return ind


if __name__ == "__main__":
    # Sample test case
    haystack = "hello"
    needle = "ll"
    sol = Solution()
    print(sol.strStr(haystack, needle))  # Expected output: 2

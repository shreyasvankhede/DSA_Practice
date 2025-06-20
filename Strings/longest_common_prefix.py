"""
Problem: Longest Common Prefix
LeetCode: https://leetcode.com/problems/longest-common-prefix/
Category: String
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix string amongst an array of strings.
        """
        if not strs:
            return ""

        # Find the shortest string's length to avoid index errors
        min_len = min(len(s) for s in strs)

        prefix = ""
        for i in range(min_len):
            current_char = strs[0][i]
            if all(s[i] == current_char for s in strs):
                prefix += current_char
            else:
                break

        return prefix


if __name__ == "__main__":
    # Sample test case
    strs = ["flower", "flow", "flight"]
    sol = Solution()
    print(sol.longestCommonPrefix(strs))  # Expected output: "fl"

"""
Problem: Valid Anagram
LeetCode: https://leetcode.com/problems/valid-anagram/
Category: Hash Table, String
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks if string t is an anagram of string s.
        """
        if len(s) != len(t):
            return False

        unique_chars = set(s)
        for char in unique_chars:
            if s.count(char) != t.count(char):
                return False

        return True


if __name__ == "__main__":
    # Sample test case
    s = "anagram"
    t = "nagaram"
    sol = Solution()
    print(sol.isAnagram(s, t))  # Expected output: True

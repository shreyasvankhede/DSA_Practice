"""
Problem: Find the Difference
LeetCode: https://leetcode.com/problems/find-the-difference/
Category: String, Bit Manipulation
Approach: XOR (Optimized O(n), O(1) space)
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Uses XOR to find the extra character in t that is not in s.
        All matching characters cancel out using XOR logic.
        """
        result = 0
        for char in s + t:
            result ^= ord(char)  # XOR all Unicode code points
        return chr(result)       # Convert the remaining code point back to character


if __name__ == "__main__":
    # Sample test case
    s = "abcd"
    t = "abcde"
    sol = Solution()
    print(sol.findTheDifference(s, t))  # Expected output: "e"

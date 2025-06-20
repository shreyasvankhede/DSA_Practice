"""
Problem: Add Binary
LeetCode: https://leetcode.com/problems/add-binary/
Category: String, Binary Math
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Convert binary strings to integers, add them, and convert the result back to binary.
        """
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    # Sample test case
    a = "11"
    b = "1"
    sol = Solution()
    print(sol.addBinary(a, b))  # Expected output: "100"

"""
Problem: Pow(x, n)
LeetCode: https://leetcode.com/problems/powx-n/
Category: Math, Recursion
Note: This uses Python's built-in exponentiation (x**n).
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Returns x raised to the power n (x^n).
        """
        return x ** n


if __name__ == "__main__":
    # Sample test case
    x = 2.00000
    n = 10
    sol = Solution()
    print(sol.myPow(x, n))  # Expected output: 1024.0

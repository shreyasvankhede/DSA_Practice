"""
Problem: Sqrt(x)
LeetCode: https://leetcode.com/problems/sqrtx/
Category: Math
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        # follows newtons method
        guess = x
        while guess * guess > x:
            guess = ((guess) + x // guess) // 2
        return guess


if __name__ == "__main__":
    # Sample test case
    x = 8
    sol = Solution()
    print(sol.mySqrt(x))  # Expected output: 2

"""
Problem: Add Digits
LeetCode: https://leetcode.com/problems/add-digits/
Category: Math, Simulation
Approach: Repeated digit sum until result is a single digit
"""

class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            total = 0
            while num != 0:
                total += num % 10
                num = num // 10
            if total < 10:
                return total
            else:
                num = total


if __name__ == "__main__":
    sol = Solution()
    print(sol.addDigits(38))   # Expected output: 2
    print(sol.addDigits(0))    # Expected output: 0
    print(sol.addDigits(99))   # Expected output: 9

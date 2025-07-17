"""
Problem: Happy Number
LeetCode: https://leetcode.com/problems/happy-number/
Category: Hashing, Math
Approach: Use a set to detect cycles in the digit-square sum sequence.
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            total = 0
            while n > 0:
                total += (n % 10) ** 2
                n = n // 10
            n = total
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.isHappy(19))   # Expected output: True
    print(sol.isHappy(2))    # Expected output: False
    print(sol.isHappy(1))    # Expected output: True

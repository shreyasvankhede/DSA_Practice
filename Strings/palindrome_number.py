"""
Problem: Palindrome Number
LeetCode: https://leetcode.com/problems/palindrome-number/
Category: Math
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Returns True if the integer is a palindrome, False otherwise.
        Negative numbers are not palindromes by default.
        """
        x_str = str(x)
        return x_str == x_str[::-1]


if __name__ == "__main__":
    # Sample test case
    x = 121
    sol = Solution()
    print(sol.isPalindrome(x))  # Expected output: True

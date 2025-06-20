"""
Problem: Valid Parentheses
LeetCode: https://leetcode.com/problems/valid-parentheses/
Category: Stack, String
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Uses a stack to check if all parentheses are closed correctly and in order.
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                return False  # Invalid character

        return not stack


if __name__ == "__main__":
    # Sample test case
    s = "()[]{}"
    sol = Solution()
    print(sol.isValid(s))  # Expected output: True

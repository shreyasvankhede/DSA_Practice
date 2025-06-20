"""
Problem: Roman to Integer
LeetCode: https://leetcode.com/problems/roman-to-integer/
Category: String, HashMap
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Converts a Roman numeral string to its integer value.
        """
        roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
        
        total = 0
        prev_value = 0

        for char in s:
            value = roman.get(char, 0)
            if value == 0:
                return "Enter valid input"

            if value > prev_value:
                total += value - 2 * prev_value
            else:
                total += value
            prev_value = value

        return total


if __name__ == "__main__":
    # Sample test case
    s = "MCMXCIV"
    sol = Solution()
    print(sol.romanToInt(s))  # Expected output: 1994

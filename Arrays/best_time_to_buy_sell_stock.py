"""
Problem: Best Time to Buy and Sell Stock
LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Category: Array, Greedy
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Track the minimum price so far and compute max profit by checking
        the difference between current price and the minimum.
        """
        mini = float('inf')
        maxi = 0

        for price in prices:
            mini = min(mini, price)
            maxi = max(maxi, price - mini)

        return maxi


if __name__ == "__main__":
    # Sample test case
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    print(sol.maxProfit(prices))  # Expected output: 5

from typing import List


# Time Limit Exceeded Error 198/211 Tests Pass
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        n = len(prices)
        for i in range(n - 1):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)

        if max_profit > 0:
            return max_profit
        else:
            return 0


# All test case pass
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit

        return max_profit


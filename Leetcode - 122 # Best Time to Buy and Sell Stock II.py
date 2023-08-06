# We will check if prices on next day is > than previous day
# Then we have profit - and add it to total profit
# Thus we will start the loop from index 1
# i.e. if prices of stock on index 1 is > prices of stock on index i-1
# then we will buy stock on i-1 and sell on i
# and calculate the profit
# and add it to total profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit = profit + (prices[i] - prices[i-1])
        return profit


# or we can start from current index
# and check if in future or next day prices is more
# if more, lets earn profit
# if not more, skip buy

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit = profit + (prices[i + 1] - prices[i])

        return profit
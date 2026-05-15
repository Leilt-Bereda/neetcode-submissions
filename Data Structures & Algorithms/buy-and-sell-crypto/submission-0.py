'''
profit = buy low, sell high
profit = sell - buy
sell < buy - no profit
l - buy = 0
r - sell = 1
[10,1,5,6,7,1]
    b     s

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)# we wanna keep track of the max profit we can get
            else:
                buy = sell
            sell += 1
        return max_profit
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
        b = 0
        res = 0
        for s in range(1, len(prices)):
            if prices[s] > prices[b]:
                res = max(res, prices[s] - prices[b])
            else:
                prices[b] = prices[s]
        return res











        # buy = 0
        # sell = 1
        # max_profit = 0

        # while sell < len(prices):
        #     if prices[sell] > prices[buy]:
        #         profit = prices[sell] - prices[buy]
        #         max_profit = max(max_profit, profit)# we wanna keep track of the max profit we can get
        #     else:
        #         buy = sell
        #     sell += 1
        # return max_profit
        
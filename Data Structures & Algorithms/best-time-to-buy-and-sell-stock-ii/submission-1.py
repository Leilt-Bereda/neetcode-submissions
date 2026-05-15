'''
buy low sell high - profit
profit = s-b
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # b = 0
        # for s in range(1, len(prices)):
        #     if prices[s] > prices[b]:
        #         max_profit += prices[s] - prices[b]
        #     b += 1
        # return max_profit
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
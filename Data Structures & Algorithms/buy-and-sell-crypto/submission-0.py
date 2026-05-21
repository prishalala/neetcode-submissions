class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=[]
        if prices==sorted(prices, reverse=True):
            return 0
        else:
            for i in range(len(prices)):
                for j in range(i+1,len(prices)):
                    profit.append(prices[j] - prices[i])
            return max(profit)

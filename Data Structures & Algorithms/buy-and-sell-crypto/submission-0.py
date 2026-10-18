class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        max_p = 0
        for i in range(l):
            for j in range(i+1,l):
                p = prices[j] - prices[i]
                if max_p < p:
                    max_p = p
        return max_p
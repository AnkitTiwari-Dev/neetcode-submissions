class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        mini = math.inf
        max_p = 0
        for i in range(l):
            if prices[i] < mini:
                mini = prices[i]
            p = prices[i] - mini
            if p > max_p:
                max_p = p
        return max_p
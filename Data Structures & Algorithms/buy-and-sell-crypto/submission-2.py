class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        res = 0
        l,r = 0,1
        while l<len(prices) and r<len(prices):
            if prices[l]>= prices[r]:
                l = r
            else:
                res = max(res, prices[r]-prices[l])
            r += 1
        return res
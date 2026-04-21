class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            max_prof = 0
            for j in range(i+1, len(prices)):
                diff = prices[j]-prices[i]
                max_prof = max(max_prof, diff)
            res = max(res, max_prof)
        return res
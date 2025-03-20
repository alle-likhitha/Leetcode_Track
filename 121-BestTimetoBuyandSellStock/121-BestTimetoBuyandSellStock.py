class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        p = 0
        for i in range(1,len(prices)):
            if prices[i] < mi:
                mi = prices[i]
            if prices[i] - mi > p:
                p = prices[i] - mi
            # print(mi, p)
        return p
// Last updated: 3/19/2025, 8:41:34 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        max_p = 0
        for j in range(1,len(prices)):
            if prices[i] > prices[j]:
                i = j
            elif prices[j] - prices[i] > max_p:
                max_p = prices[j] - prices[i]
        
        return max_p

        mi = prices[0]
        p = 0
        for i in range(1,len(prices)):
            if prices[i] < mi:
                mi = prices[i]
            if prices[i] - mi > p:
                p = prices[i] - mi
            # print(mi, p)
        return p

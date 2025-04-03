# Last updated: 4/2/2025, 7:47:28 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        temp1 = cost[-1]
        temp2 = cost[-2]
        res = min(cost[-1], cost[-2])
        for i in range(len(cost)-3,-1,-1):
            res = min(temp1+ cost[i], temp2+cost[i])
            temp1 = temp2
            temp2 = res
            # print(res)
        # return min(stack[-1], stack[-2])
        return min(res, temp1)
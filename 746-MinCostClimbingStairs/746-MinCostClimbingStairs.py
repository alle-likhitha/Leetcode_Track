# Last updated: 4/2/2025, 7:40:28 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        stack = [cost[-1], cost[-2]]
        for i in range(len(cost)-3,-1,-1):
            stack.append(cost[i] + min(stack[-1], stack[-2]))
            # print(stack)
        return min(stack[-1], stack[-2])
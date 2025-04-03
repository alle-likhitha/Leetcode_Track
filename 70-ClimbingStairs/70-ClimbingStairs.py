# Last updated: 4/2/2025, 7:00:55 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        stack = [1,2]
        if n <=2:
            return stack[n-1]
        for i in range(2,n):
            stack.append(stack[i-1] + stack[i-2])
        # print(stack)

        return stack[-1]
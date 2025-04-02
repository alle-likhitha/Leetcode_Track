# Last updated: 4/1/2025, 8:03:10 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        stack = [0]
        res = [0] * len(temperatures)
        for i in range(1,len(temperatures)):
            # print(res, i, temperatures[i], stack)
            while stack != [] and temperatures[stack[-1]] < temperatures[i]:
                k = stack.pop()
                res[k] = i - k
            stack.append(i)
            # print(res, i, temperatures[i], stack)
        return res

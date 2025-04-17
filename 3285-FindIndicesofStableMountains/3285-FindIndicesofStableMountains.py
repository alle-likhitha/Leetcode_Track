# Last updated: 4/16/2025, 8:39:12 PM
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        stack = False
        res = []
        for i in range(len(height)):
            if stack:
                res.append(i)
            if height[i] > threshold:
                stack = True
            else:
                stack = False
            # print(res)
        return res
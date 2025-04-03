# Last updated: 4/2/2025, 5:40:23 PM
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        right_max = [0] * len(nums)
        right_max[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i])
        # print(right_max)
        stack = []
        res = 0

        for i in range(len(nums) - 1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            stack.append(nums[i])
            if stack:
                res = max(res, ((stack[0] - stack[-1]) * right_max[i+1]))
            # print(res)
        return res
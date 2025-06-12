# Last updated: 6/11/2025, 8:30:05 PM
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxad = abs(nums[0] - nums[-1])
        # print(maxad)
        i = 0
        j = 1
        while j < len(nums):
            if abs(nums[i] - nums[j]) > maxad:
                maxad = abs(nums[i] - nums[j])
            i = j
            j += 1
            # print(maxad)
        return maxad
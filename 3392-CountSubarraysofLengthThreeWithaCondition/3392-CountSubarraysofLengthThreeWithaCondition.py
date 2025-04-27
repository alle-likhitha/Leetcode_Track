# Last updated: 4/27/2025, 4:27:33 PM
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        i = 0
        for j in range(2, len(nums)):
            if (nums[i] + nums[j]) == (nums[i+1] / 2):
                count += 1
            i += 1
            print(count)

        return count
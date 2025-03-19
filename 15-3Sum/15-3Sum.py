class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        m = {}
        res = []
        nums.sort()
        for k in range(len(nums)):
            target = -1 * nums[k]
            i = k + 1
            j = len(nums) - 1
            while i < j:
                p = target - nums[j]
                if p == nums[i]:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                elif p > nums[i]:
                    i += 1
                elif p < nums[i]:
                    j -= 1
        # res = list(set(res))
        unique_data = [list(t) for t in {tuple(lst) for lst in res}]
        return unique_data
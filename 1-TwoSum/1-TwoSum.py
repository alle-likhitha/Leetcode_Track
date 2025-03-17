class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, num in enumerate(nums):
            # print(i,num)
            tar2 = target - num
            if tar2 in m:
                return [i, m[tar2]] 
            else:
                m[num] = i
        return []

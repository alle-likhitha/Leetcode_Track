class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(set(nums))
        m = 0
        temp_c = 1
        seen = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == seen + 1:
                seen = nums[i]
                temp_c += 1
            else:
                if m <= temp_c:
                    m = temp_c
                temp_c = 1
                seen = nums[i]
            # print(nums, temp_c, m, seen, i)
        if m == 0 or m <= temp_c:
            m = temp_c
        print(m)
        return m
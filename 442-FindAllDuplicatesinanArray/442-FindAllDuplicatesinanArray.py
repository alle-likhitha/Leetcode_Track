class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        m = {}
        k = []
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                k.append(i)
        return k
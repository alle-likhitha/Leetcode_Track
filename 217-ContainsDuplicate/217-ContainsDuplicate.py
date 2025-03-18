class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num2 = {}
        for i in nums:
            if i not in num2:
                num2[i] = 1
            else:
                # num2[i] += 1
                return True
        # print(num2)
        return False


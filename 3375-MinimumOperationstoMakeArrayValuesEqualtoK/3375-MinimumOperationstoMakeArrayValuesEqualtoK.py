# Last updated: 4/9/2025, 4:31:57 PM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int: 
        ans = set()
        for i in nums:
            if i > k:
                ans.add(i)
            if i < k:
                return -1

        return len(ans)
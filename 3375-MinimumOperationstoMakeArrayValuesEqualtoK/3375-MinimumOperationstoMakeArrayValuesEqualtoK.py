# Last updated: 4/9/2025, 2:57:42 PM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(i < k for i in nums):
            return -1  
        
        ans = set()
        for i in nums:
            if i > k:
                ans.add(i)

        return len(ans)
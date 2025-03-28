# Last updated: 3/27/2025, 7:47:37 PM
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        max_num = []
        for i, n in enumerate(nums):
            # print('i = ',i,'n = ',n)
            while d and nums[d[-1]] < n:
                d.pop()
                # print('Popped from d cuz no use', d)
            d.append(i)
            # print('i added to d', d)
            if d[0] == i - k:
                d.popleft()
                # print('popped cuz out of window', d)
            if i >= k-1:
                max_num.append(nums[d[0]])
                # print('Updated maxnums',max_num)
        return max_num
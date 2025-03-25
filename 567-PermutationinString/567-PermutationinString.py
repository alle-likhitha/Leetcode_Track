# Last updated: 3/24/2025, 7:30:13 PM
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 = Counter(s1)
        s2_count = {}
        i = 0
        for j in range(len(s2)):
            # print('before',s2_count, i, j)
            if s2_count == s1:
                return True
            if j-i+1 > n:
                s2_count[s2[i]] -= 1
                if s2_count[s2[i]] == 0:
                    s2_count.pop(s2[i])
                i += 1
            s2_count[s2[j]] = s2_count.get(s2[j], 0) + 1
            # print('after',s2_count, i, j)
        if s2_count == s1:
            return True
        return False
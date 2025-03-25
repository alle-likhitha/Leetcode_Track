# Last updated: 3/24/2025, 6:37:07 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        max_l = 0
        temp_set = set()
        for j in range(len(s)):
            while s[j] in temp_set:
                temp_set.remove(s[i])
                i += 1
            temp_set.add(s[j])
            max_l = max(max_l, j-i+1)
        return max_l
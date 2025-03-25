# Last updated: 3/24/2025, 6:28:56 PM
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        my_dict = {}
        temp = k #1
        max_val = 0

        for char in s: #AABAB
            my_dict[char] = my_dict.get(char, 0) + 1 #A:3 B:2 A:2
            if my_dict[char] > max_val: # 1>0 2>1 3>2 
                max_val = my_dict[char] # 1 2 3
            else:
                temp -= 1 # 0 -1 
                if temp < 0: 
                    my_dict[s[start]] -=1 #A:2
                    start += 1 #1
                    temp = 0 #0
        return max_val + k - temp

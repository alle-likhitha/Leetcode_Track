# Last updated: 3/25/2025, 7:37:43 PM
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        t_dict = Counter(t)  # Frequency of characters in t
        window = {}
        
        left = 0
        min_len = float("inf")
        min_substr = ""
        
        required = len(t_dict)  # Number of unique chars in t that must match
        formed = 0  # Number of unique chars in current window matching the required frequency

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in t_dict and window[char] == t_dict[char]:
                formed += 1
            
            # Try shrinking the window
            while left <= right and formed == required:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    min_substr = s[left:right + 1]
                
                # Remove leftmost character from window
                window[s[left]] -= 1
                if s[left] in t_dict and window[s[left]] < t_dict[s[left]]:
                    formed -= 1

                left += 1  # Move the left pointer

        return min_substr

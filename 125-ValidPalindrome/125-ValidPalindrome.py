class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip()
        if not s: return True

        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.replace(" ", "").lower()
        return s == s[::-1]
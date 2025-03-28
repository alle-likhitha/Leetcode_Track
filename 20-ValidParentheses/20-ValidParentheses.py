# Last updated: 3/27/2025, 8:02:32 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        temp = 0
        m = {'(':')', '{':'}', '[':']'}
        right = 0
        for i in s:
            if i in m:
                temp = 1
                stack.append(i)
            elif i in m.values() and stack != []:
                x = stack.pop()
                if (i == ')' and x != '(') or (i == '}' and x != '{') or (i == ']' and x != '['):
                    return False
            else:
                right += 1
        if stack == [] and temp == 1 and right == 0:
            return True
        return False

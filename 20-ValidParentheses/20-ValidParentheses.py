# Last updated: 3/27/2025, 7:51:50 PM
class Solution:
    def isValid(self, s: str) -> bool:
        m = ['(','{','[']
        n = [')','}',']']
        stack = []
        v = 0
        for i in s:
            if i in m:
                stack.append(i)
                v = m.index(i)
                # print(stack)
            else:
                if i == n[v] and stack != []:
                    stack.pop()
                    # print(stack)
                    if stack == []:
                        v = 0
                    else:
                        v = m.index(stack[-1])
                else:
                    return False
        if stack == []:
            return True
        else:
            False
# Last updated: 7/27/2025, 6:12:15 PM
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        for q,t in sorted(((x,'ab'),(y,'ba')))[::-1]:
            # print(q,t)
            stack = []
            for ch in s:
                
                if stack and stack[-1]+ch == t:
                    res += q
                    stack.pop()
                else:
                    stack.append(ch)
                # print(stack, ch, q, res)
            s = stack

        return res
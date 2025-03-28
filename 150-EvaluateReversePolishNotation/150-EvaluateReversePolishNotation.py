# Last updated: 3/27/2025, 8:30:20 PM
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def oper(x,y,t):
            if t == "+":
                return y+x
            elif t == "*":
                return y * x
            elif t == "-":
                return y - x
            else:
                return (math.trunc(y/x))
        m = ["+","-","*","/"]
        stack = []
        for i in tokens:
            if i in m:
                x = stack.pop()
                y = stack.pop()
                x = oper(x,y,i)
                stack.append(x)
            else:
                stack.append(int(i))
        return stack[0]
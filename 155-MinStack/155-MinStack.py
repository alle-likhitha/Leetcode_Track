# Last updated: 3/27/2025, 8:20:49 PM
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minstack:
            prevmin = self.minstack[-1]
            self.minstack.append(min(val,prevmin)) 
        else:
            self.minstack.append(val)

    def pop(self) -> None:
        self.minstack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
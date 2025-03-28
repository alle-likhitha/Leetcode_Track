# Last updated: 3/27/2025, 8:20:11 PM
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []

    def push(self, x: int) -> None:
        count = self.getMin()
        if self.items == [] or x < count:
            count = x
        self.items.append((x, count))
        # print(self.items)

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        if self.items == []:
            return None
        else:
            return self.items[-1][0]

    def getMin(self) -> int:
        if self.items == []:
            return None
        else:
            return self.items[-1][1]

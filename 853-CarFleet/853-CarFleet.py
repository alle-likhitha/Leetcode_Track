# Last updated: 4/2/2025, 6:16:48 PM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [[p,s] for p, s in zip(position, speed)]
        pos_speed = sorted(pos_speed)[::-1]
        # print(pos_speed)

        stack = []
        for p, s in pos_speed:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            # print(stack)
        return len(stack)
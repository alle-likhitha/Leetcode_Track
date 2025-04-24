# Last updated: 4/23/2025, 6:14:24 PM
class Solution:
    def countLargestGroup(self, n: int) -> int:
        def count_digit(k):
            c = 0
            while k > 0:
                c += k % 10
                k = k // 10
                # print(k)
            return c

        d = {}
        for i in range(1,n+1):
            dsum = count_digit(i)
            if dsum in d:
                d[dsum] += 1
            else:
                d[dsum] = 1
            # print(d, dsum)
        d_values = list(d.values())
        # print(d_values)
        maxind = max(d_values)
        max_count = d_values.count(maxind)
        # print(max_count)
        
        return max_count
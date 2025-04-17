# Last updated: 4/16/2025, 8:13:35 PM
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        def check(di, newi, k):
            c = 0
            # print(di, newi, k)
            for j in di:
                if (j * newi) % k == 0:
                    c += 1
                    # print('inside if',c)
            return c

        d = defaultdict(list)
        res = 0
        for i in range(len(nums)):
            if nums[i] in d:
                res += check(d[nums[i]], i, k)
                d[nums[i]].append(i)
            else:
                d[nums[i]].append(i)
            # print(res)
            # print(d)

        return res
        
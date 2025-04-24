# Last updated: 4/24/2025, 1:00:51 AM
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        def check(d):
            x = list(d.values())
            # print('in check', list(d.values()))
            for i in x:
                
                if i == 0:
                    return False
            # print(True)
            return True

        we_need = list(set(nums))
        d = {}
        for i in we_need:
            d[i] = 0
        i = 0
        # j = 0
        l = len(nums)
        count = 0

        for j in range(l):
            d[nums[j]] += 1
            if check(d) == True:
                count += l - j 
                # print('j true i,j = ',i, j , count)
                d[nums[i]] -= 1
                i += 1
                # while(check(d) == True):
                while d[nums[i-1]] != 0:
                    count += l - j
                    # print('i dec',i, count)
                    d[nums[i]] -= 1
                    if d[nums[i]] == 0:
                        i += 1
                        break
                    # print(d)
                    i += 1
            # print('out',count)
            # print('out',d)

        return count
            
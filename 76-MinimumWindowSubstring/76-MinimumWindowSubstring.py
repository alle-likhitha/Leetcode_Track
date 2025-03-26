# Last updated: 3/25/2025, 7:54:14 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if s == t:
            return t
        in_st_dict = {}
        t_dict = {}
        # res = []
        result = ""
        temp_to_check = True
        i = 0
        j = 0
        for tt in range(len(t)):
            t_dict[t[tt]] = t_dict.get(t[tt], 0) + 1
            
       
        while(j < len(s) and i < len(s)):
            # print(i,j)
        # for j in range(len(t),len(s)):
            temp_to_check = True
            if s[j] in t:
                in_st_dict[s[j]] = in_st_dict.get(s[j], 0) + 1
            # temp_to_check = True
            
            for key, val in t_dict.items():
                if key not in in_st_dict or val > in_st_dict[key]:
                    temp_to_check = False
                    break

            while(temp_to_check):
                while s[i] not in t:
                    i += 1
            
                if result == "":
                    result = s[i:j+1]
                elif len(result) > j - i + 1:
                    result = s[i:j+1]
                in_st_dict[s[i]] -= 1

                if in_st_dict[s[i]] == 0:
                    in_st_dict.pop(s[i])
                i += 1
                
                for key, val in t_dict.items():
                    # print(t_dict,'items in t')
                    # print(in_st_dict, 'items in new st dict')
                    if key not in in_st_dict or val > in_st_dict[key]:
                        temp_to_check = False
                        break
                    

            # print(i,j)
            j += 1
        # print(res)
        # print(result)
        return result
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        l = len(s)
        l2 = len(t)
        if l != l2:
            return False
        
        for i in range (0, l):
            a = s[i]
            j= 0
            while j < l2:
                b = t[j]
                if a == b:
                    t = t[:j]+ t[j+1 :]
                    break
                l2 = len(t)
                j=j+1
            print(t)

        if t == "":
            return True
        else:
            return False
            '''
        l = len(s)
        l2 = len(t)
        if l != l2:
            return False
        dic_s = {}
        dic_t = {}
        for i in range (l):
            dic_s[s[i]] = 1 + dic_s.get(s[i], 0)
            dic_t[t[i]] = 1 + dic_t.get(t[i], 0)
        return dic_t == dic_s


        
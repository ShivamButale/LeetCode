class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        k_dict = {}
        i = 0
        j = 0 
        l = list(s.split(' '))
        if len(pattern) != len(l):
            return False
        while(i<len(pattern) and j<len(l)):
            try:
                a = k_dict[pattern[i]]
                if l[j] != a:
                    return False
                else:
                    i+=1
                    j+=1
            except:    
                if l[j] in k_dict.values():
                    return False
                k_dict[pattern[i]] = l[j]
                i+=1
                j+=1

        return True
            

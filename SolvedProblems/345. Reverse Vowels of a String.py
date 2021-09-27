class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','A','e','E','i','I','o','O','u','U']
        l = []
        ind = []
        s1 = list(s)
        for i in range(0, len(s)):
            if s[i] in vowels:
                ind.append(i)
                l.append(s[i])
        l.reverse()
        i=0
        while i<len(l):
            s1[ind[i]] = l[i]
            i += 1
        return ''.join(s1)

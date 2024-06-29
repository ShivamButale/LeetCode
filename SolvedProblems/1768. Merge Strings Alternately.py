class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i =0 
        j = 0
        final = ""
        while i<len(word1) and j<len(word2):
            final += word1[i]
            final += word2[j]
            i+=1
            j+=1
            

        if i < len(word1):
            while i<len(word1):
                final += word1[i]
                i+=1

        if j<len(word2):
            while j<len(word2):
                final += word2[j]
                j+=1

        return final 

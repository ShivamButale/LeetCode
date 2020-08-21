class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        solution = []
        
        word_pool = set(wordDict)
        
        if set(s) > set(''.join(wordDict)):
            return []
        
        def helper(s,words):
            if s== "":
                solution.append(' '.join(words))
                return 
            
            for prefix in word_pool:
                if len(prefix) > len(s):
                    continue
                    
                if s.startswith(prefix):
                    helper(s[len(prefix):], words[:]+[prefix])
            return 
    
        helper(s, words = [])
        return solution
    

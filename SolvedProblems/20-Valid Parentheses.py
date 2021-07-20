class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapp = {')' : '(', '}':'{', ']':'['}
        for i in s:
            if i in mapp.values():
                stack.append(i)
            else:
                if len(stack)==0:
                    return False
                if(stack[-1] != mapp[i]):
                    return False
                else:
                    stack.pop()
        if len(stack)>0:
            return False
        return True

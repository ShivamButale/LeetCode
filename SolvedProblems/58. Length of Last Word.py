class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s is None:
            return 0
        s = s.rstrip()
        x = s.split(" ")
        return len(x[-1])

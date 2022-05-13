class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        init = sum(arr)
        nxt = 3
        n = len(arr)
        while(n >= nxt):
            for i in range(0, len(arr) - nxt+1):
                init += sum(arr[i: i+nxt])
            nxt += 2

        return init 

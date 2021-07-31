class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        ways = []
        ways.append(1)
        ways.append(1)
        ways.append(2)
        for i in range(3, n+1):
            ways.append(ways[i-1] + ways[i-2])
        return ways[n]
    

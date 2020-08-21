class Solution:
    def reverseBits(self, n: int) -> int:
        sol = 0
        for i in range(0, 32):
            AND = n & 1
            n = n >> 1
            sol = sol << 1
            sol = sol + AND
        return sol

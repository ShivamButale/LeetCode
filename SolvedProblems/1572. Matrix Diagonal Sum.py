class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s1 = 0
        for i in range(0, n):
            s1 += mat[i][i] + mat[i][n-i-1]
            
        if n%2==1:
            k = n//2
            s1 -= mat[k][k]
        return s1
            

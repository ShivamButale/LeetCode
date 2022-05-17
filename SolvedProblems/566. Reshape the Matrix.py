class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        if rows*cols != r*c:
            return mat 
        
        l = []
        for i in range(0, rows):
            curr_row = mat[i]
            for z in curr_row:
                l.append(z)
        
        final  = []
        t = len(l)
        
        a = 0
        b = c
        while t:
            arr = []
            for x in range(a, b):
                arr.append(l[x])  
            final.append(arr)
            t = t - c
            a = a + c
            b = b + c
            
        return final 
        

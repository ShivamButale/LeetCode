class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0

        m = len(grid)
        n = len(grid[0])
        
        def process_index(i, j):
            if i <= 0 or i >= m or j <= 0 or j >= n:
                pass 
            
        visited = set()
        for i in range(m):
            for j in range(n):
                if m[i][j] != 1:
                    pass 
                else:
                    visited.append(i, j)
                    process_index(i, j)


        return numIslands 

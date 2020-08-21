class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def checkNeighbours(i, j, val):
            if i!=len(grid)-1 and grid[i+1][j]==1: #Bottom
                val =val -1
            if i!=0 and grid[i-1][j]==1: #Top
                val -= 1
            if j!=0 and grid[i][j-1]==1: #Left
                val -= 1 
            if j!=len(grid[0])-1 and grid[i][j+1]==1: #Right
                val -= 1
            return val
        
        p = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    val = checkNeighbours(i, j, 4)
                    p = p+ val
                else:
                    pass
        return p

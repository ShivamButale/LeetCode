class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
       nc = 0

       #Since matrix is sorting in descending order - both row-wise and column-wise 
       #Best strategy would be to travel from top right as we can break when we find a postive number 
       # and proceed to next row directly . Also if we find a negative number, we can safely be sure all numbers
       # below it are negative 

       i = 0
       j = len(grid[0]) - 1
       
       while (i < len(grid) and j >= 0):
            if grid[i][j] < 0:
                nc += len(grid) - i
                j -= 1
            else:
                i += 1
    
       return nc

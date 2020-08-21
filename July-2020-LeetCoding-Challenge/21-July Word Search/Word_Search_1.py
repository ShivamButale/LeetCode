class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return  False 
        
        height = len(board)
        width = len(board[0])
        
        def dfs(index, x, y):
            if x<0 or x==width or y<0 or y==height or word[index]!=board[y][x]:
                return False
            
            if index==len(word)-1:
                return True 
            
            curr = board[y][x]
            
            board[y][x] = '#'
            
            visited = dfs(index+1,x+1,y) or dfs(index+1,x-1,y) or dfs(index+1,x,y+1) or dfs(index+1,x,y-1)
            
            board[y][x] = curr
            
            return visited
        
        return any(dfs(0,x,y) for y in range(height) for x in range(width))
            

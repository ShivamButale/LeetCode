class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        day = 0
        new = [0]*8
        new_1 = None
        
        while(N):
            for i in range(1, 7):
                if cells[i-1]==cells[i+1]:
                    new[i] = 1
                else:
                    new[i] = 0 
            
            if day==0:
                new_1 = new[:]
            elif new==new_1:
                N %= day
                
            cells = new[:]
            day = day +1
            N-=1
        return new

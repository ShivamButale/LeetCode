class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [[1]]
        if numRows==1:
            return l
        
        l = [[1], [1,1]]
        if numRows==2:
            return l
        
        l = [[1], [1,1], [1,2,1]]
        if numRows==3:
            return l
        
        for i in range(3, numRows):
            li = []
            li.append(1)

            prev = l[i-1]
            for j in range(len(prev)-1):
                li.append(prev[j]+prev[j+1])
                
            li.append(1)
            l.append(li)
            
        return l

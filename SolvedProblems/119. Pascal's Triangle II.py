class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l = [[1]]
        if rowIndex==0:
            return l[0]
        
        l = [[1], [1,1]]
        if rowIndex==1:
            return l[1]
        
        l = [[1], [1,1], [1,2,1]]
        if rowIndex==2:
            return l[2]
        
        for i in range(3, rowIndex+1):
            li = []
            li.append(1)

            prev = l[i-1]
            for j in range(len(prev)-1):
                li.append(prev[j]+prev[j+1])
                
            li.append(1)
            l.append(li)
            
        return l[rowIndex]

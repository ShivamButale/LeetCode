class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(0, len(flowerbed)):
            if n==0:
                return True

            if flowerbed[i]==1:
                continue
            else:
                if i>0:
                    if flowerbed[i-1] == 1:
                        continue 
                
                if i < len(flowerbed)-1:
                    if flowerbed[i+1]==1:
                        continue 
                
                n-=1
                flowerbed[i] = 1
    
        if n==0:
            return True        


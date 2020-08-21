class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #print("a = ", a, " b = ", b)
        '''
        list_a = []
        for i in a:
            list_a.append(int(i))
        #print("LIST A = ", list_a)
        n = len(list_a)
        
        #DECIMAL A
        dec_a = 0
        index = 0
        for i in range(n-1, -1, -1):
            dec_a += list_a[i] * (2**(index))
            #print("Index = ", i, " DECIMAL A = ", dec_a)
            index = index + 1
        #print(dec_a)
        
        list_b = []
        for i in b:
            list_b.append(int(i))
        #print("LIST B = ", list_b)
        n = len(list_b)
        
        #DECIMAL B
        dec_b = 0
        index = 0
        for i in range(n-1, -1, -1):
            dec_b += list_b[i] * (2**(index))
            #print("Index = ", i, " DECIMAL A = ", dec_b)
            index = index + 1
        #print(dec_b)
        
        dec_sum = dec_a + dec_b
        #print("DECIMAL SUM = ", dec_sum)
        
        
        #Convert decimal to binary
        if dec_sum == 0:
            return 0
        if dec_sum == 1:
            return 1
        rems = []
    
        q = -1
        while(q != 0):
            q = dec_sum // 2
            r = dec_sum % 2
            rems.append(r)
        
        rems.reverse()
        print(rems)
        '''
        print("a = ", a, " b= ", b)
        
        list_a = []
        for i in a:
            list_a.append(int(i))
        print("LIST A = ", list_a)
        n = len(list_a)
        
        list_b = []
        for i in b:
            list_b.append(int(i))
        print("LIST B = ", list_b)
        n2 = len(list_b)
        
        a = list_a
        b = list_b 
        print("LENGTH of A = ", len(a))
        print("LENGTH OF B = ", len(b))
        
        small_length = min(n, n2)
        big_length = max(n, n2)
        
        index = -1
        sum = []
        
        while (small_length):
            print("CURRENT SUM from a and b= ", a[index] + b[index])
            sum.append(a[index] + b[index])
            index = index - 1
            small_length -= 1
            big_length -= 1
        
        if n > n2:
                while big_length:
                    print("CURRENT SUM from a = ", a[index])
                    sum.append(a[index])
                    index = index - 1
                    big_length -= 1
        else:
                while big_length:
                    print("CURRENT SUM from b = ", b[index])
                    sum.append(b[index])
                    index = index - 1
                    big_length -= 1
                
        
        print(sum)
        
        for i in range(0, len(sum)):
            if sum[i] == 2:
                sum[i] = 0
                if i == len(sum)-1:
                    sum.append(0)
                sum[i+1] = sum[i+1]+1
            if sum[i] == 3:
                sum[i] = 1
                if i == len(sum)-1:
                    sum.append(0)
                sum[i+1] = sum[i+1]+1
                
                
        print(sum)
        sum.reverse()
        print(sum)
        str1=""
        for i in sum:
            str1 += str(i)
        return str1

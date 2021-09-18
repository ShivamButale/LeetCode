# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        h = n
        while(l<=h):
            mid = l + (h-l)//2
            ret = isBadVersion(mid)
            if ret==True:
                prev = isBadVersion(mid-1)
                if prev==False:
                    return mid 
                else:
                    h = mid-1        
            else:
                l = mid+1


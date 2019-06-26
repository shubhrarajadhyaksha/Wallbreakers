class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        if n%2!=0 or n<1:
            return False
        
        while(n%2==0):
            
            if n==2:
                return True
            n=n/2
        return False

#Note: Divide into cases: 
#If n==1, then it is power of 2
#If n is 0 or lesser it cannot be power of 2
#If n>=2 it should be divisible by two and should return 2 at some point if we keep dividing it by 2
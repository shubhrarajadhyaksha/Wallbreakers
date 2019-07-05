class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        if n==1:
            return True
        seen_items=set()
        
        
        while 1:
            
            
            if n in seen_items:
                return False
            seen_items.add(n)
            s=0
            l=len(str(n))
            # print("length=",l)
            for i in range(l):
                # print("***")
                # print("n=",n)
            
                x=n%10
                # print("x1=",x)
                s=s+x*x
                n=(n-x)//10
            # print ("---",s)
            n=s
            if n==1:
                return True
                
                
                
 # Just thought of using seen_items so as not to get stuck in a loop  of any kind, everything else is very simple.               
            
            
            
            
                
        
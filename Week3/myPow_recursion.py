class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def get(N,ans,prod):
            # print(N,ans,prod)
            if N==0:
                # print(ans)
                return ans
            if N%2==1:
                ans=ans*prod
            # print("lalala")    
            prod=prod*prod
            ans=get(N//2,ans,prod)
            return ans
        if (n<0):
            x=1.0/x
            n=-n
        ans=get(n,1,x)
            
        
       
        
        return ans
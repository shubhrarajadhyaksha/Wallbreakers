class Solution(object):
    profit=0 
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==1:
            return 0 
        mn=None
        mx=0
        # profit=0 
        # mx=None 
        
        l=len(prices)
        
        def prices_recursion(start,end,mn):
            # print(start,mn)
            
            if start>=l-1:
                # print("here")
                if mn==None:
                    return 0
                # print(max(profit,0))
                return max(self.profit,0)
                
            # mx=prices[end]
            if start==0:
                mn=prices[start]
                self.profit=prices[end]-mn
                    
            else:
                
                mn=min(mn,prices[start])
                self.profit=max(self.profit,prices[end]-mn)
            prices_recursion(start+1,end+1,mn)
            # print(profit)
            
            
        prices_recursion(0,1,mn)
        if self.profit<0:
            return 0 
        return self.profit
        
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         mn=None
        
#         profit=0
        
#         for i in range(0,len(prices)):
#             if mn==None:
#                 mn=prices[i]
#             elif prices[i]<mn:
#                 mn=prices[i]
#             p=prices[i]-mn
#             if p>profit:
#                 profit=p
                
#         return profit
            
        
        
#         i,j=0,len(prices)-1
#         mn=None
#         mx=None
        
#         while(j>i):

            
        
        
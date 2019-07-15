class Solution(object):
    # profit=0 
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==0:
            return 0 
        mn=prices[0]
        prices[0]=0
        
        for i in range(1,len(prices)):
            mn=min(mn,prices[i])
            prices[i]=max(prices[i-1],prices[i]-mn)
            
        return prices[len(prices)-1]
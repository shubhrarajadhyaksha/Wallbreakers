class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        cash_you_have={5:0,10:0,20:0}
        
        
        for nums in bills:
            cash_you_have[nums]+=1
            
            cash_back=nums-5
            if cash_back==0:
                continue 
                
            while(cash_back>0):
                if cash_back>10:
                    if cash_you_have[10]>0:
                        cash_back-=10 
                        cash_you_have[10]-=1
                    elif cash_you_have[5]>0:
                        cash_back-=5
                        cash_you_have[5]-=1
                    else: 
                        return False 
                else:
                    if cash_you_have[5]>0:
                        cash_back-=5
                        cash_you_have[5]-=1
                    else:
                        return False 
        return True 
                        
        
                
            
        
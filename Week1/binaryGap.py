class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        max_dist=0
        found=False
        ctr=0
        i=0
        while(i<=31):
            
            x=(N&(1<<i))>>i
            # print(x)
            # print("max",max_dist)
            if x==1:
                ctr+=1
                if not found:
                    found=True
                    ctr=0
                    
                else:
                    if max_dist==None:
                        max_dist=ctr
                    else:
                        max_dist=max(max_dist,ctr)
                    ctr=0
            else:
                ctr+=1
            i+=1
                
        return max_dist
                    
        
        
#I just went through all the bits and kept track of 1's 
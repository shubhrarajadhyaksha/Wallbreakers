class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last_occurance=dict()
        ret=[]
        for index,letter in enumerate(S):
            last_occurance[letter]=index
            
        end=0 
        new=True
        count=0
        for index in range(len(S)):
            if new:
                count=1
                end=last_occurance[S[index]]
                new=False
                if index==end:
                    ret.append(count)
                    new=True
                
            else:
                count+=1
                if index==end:
                    ret.append(count)
                    new=True
                    
                    
                end_index=last_occurance[S[index]]
                if end_index>end:
                    end=end_index
                    
        return ret
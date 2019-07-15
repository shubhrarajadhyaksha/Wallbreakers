class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals or len(intervals)==1:
            return intervals
        intervals=sorted(intervals,key=lambda x:x[0])
        
        start,end=intervals[0][0],intervals[0][1]
        output=[]
        for i in range(1,len(intervals)):
            st,en=intervals[i][0],intervals[i][1]
            
            if st<=end:
                end=max(en,end)
                
            elif st>end:
                output.append([start,end])
                end=en
                start=st
                
        output.append([start,end])
                
        return output
        
        
        
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0 
        
        points=sorted(points,key=lambda x:(x[1]))
        # print(points)
        arrows=1
        start=points[0][0]
        end=points[0][1]
        for i in range(1,len(points)):
            st,en=points[i][0],points[i][1]
            
            if end<st:
                arrows+=1
                end=en
                
        return arrows
                
        
        
        
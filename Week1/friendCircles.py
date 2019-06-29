class Solution(object):
    def find(self,parents,item):
        if parents[item]==None:
            return item
        return self.find(parents,parents[item])
    
    def union(self,parents,x,y):
        x_parent=self.find(parents,x)
        y_parent=self.find(parents,y)
        if x_parent!=y_parent:
            parents[x_parent]=y_parent
        
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        parents=[None for i in range(len(M))]
        for i in range (len(M)):
            for j in range(len(M)):
                if M[i][j]==1:
                    if i!=j:
                        self.union(parents,i,j)
                        
        # print(parents)
        answer=0
        for i in range(len(parents)):
            if parents[i]==None:
                answer+=1
        return answer


#Note: Just followed the resource to understand union and find 
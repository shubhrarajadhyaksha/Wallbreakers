class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        visited=[0]*numCourses
        
        def create_graph():
            graph=dict()
            for items in range(numCourses):
                graph[items]=[]
                
            for items in prerequisites:
                x,y=items
                graph[y].append(x)
                
            return graph
        
        graph=create_graph()
        stack=[]
        possible=True
        
        def dfs(course,possible):
            # global possible
            visited[course]=-1
            if not possible:
                return 
            for i in graph[course]:
                if visited[i]==-1:
                    possible=False
                    
                if visited[i]==0:
                    possible=dfs(i,possible)
                    
            stack.append(course)
            visited[course]=1
            return possible
            
            
            
            
            
        
        for items in range(numCourses):
            if visited[items]==0:
                possible=dfs(items,possible)
                if not possible:
                    return []
                
                
        return stack[::-1]
                
                
                
        
        
        
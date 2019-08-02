
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def create_graph():
            graph=dict()
            for item in range(numCourses):
                graph[item]=[]
                
            for item in prerequisites:
                x,y=item
                graph[x].append(y)
            return(graph)
        
        def dfs(vertex,visited):
            #if vertex is already visited and cycle is present
            if visited[vertex]==-1:
                return False 
            
            # If this vertex is already traced and there is no cycle 
            if visited[vertex]==1:
                return True 
            
            visited[vertex]=-1
            
            for items in graph[vertex]:
                if not dfs(items,visited):
                    return False 
                
            visited[vertex]=1
            return True 
            
                
                
        graph=create_graph()
        print(graph)
        visited=[0]*numCourses
        for items in graph:
            # print(graph)
            if not dfs(items,visited):
                return False
            # print(graph)
        return True 
        
        
            
        
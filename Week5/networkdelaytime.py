class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        dist={node:None for node in range(1,N+1)}
        graph={node:[] for node in range(1,N+1)}
        
        for source,dest,time in times:
            graph[source].append((time,dest))
        
        # print(graph)
        # print(dist)
        
        def dfs(node,cost):
            # print("lalala")
            if dist[node]==None:
                dist[node]=cost
                # print(dist)
                
            elif dist[node]<=cost:
                return 
            
            # else:
            dist[node]=cost
            for time,n in sorted(graph[node]):
                dfs(n,time+cost)
                # return 
            
        dfs(K,0)
        # print(graph)
        # print(dist)
        
        for item in dist:
            if dist[item]==None:
                return -1
            
        else: 
            return max(dist.values())
        
            
            
        
        
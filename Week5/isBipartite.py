class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        colors={}
        
        for node in range(len(graph)):
            if node not in colors:
                colors[node]=True
                stack=[node]
                
                while stack:
                    # print("stack is ",stack)
                    item=stack.pop()
                    # print("item is ",item)
                    # print("colors=",colors)
                    for neighbor in graph[item]:
                        # print("neighbor is",neighbor)
                        if neighbor not in colors:
                            colors[neighbor]=not colors[item]
                            stack.append(neighbor)
                            
                        elif colors[neighbor]==colors[item]:
                            return False 
                        
        return True
                
        
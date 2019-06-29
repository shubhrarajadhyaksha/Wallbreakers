class Solution(object):
    def dfs(self,grid,r,c):
        rows=len(grid)
        cols=len(grid[0])
        if r not in range(rows):
            return
        if c not in range(cols):
            return 
        if grid[r][c]=="0":
            return 
        grid[r][c]="0"
        self.dfs(grid,r-1,c)
        self.dfs(grid,r+1,c)
        self.dfs(grid,r,c-1)
        self.dfs(grid,r,c+1)
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid==None or len(grid)==0:
            return 0 
        rows=len(grid)
        cols=len(grid[0])
        islands=0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    islands+=1
                    self.dfs(grid,r,c)
                    
        return islands
'''
I found this problem very hard to do using union find. I tried it for lot of time. It used to pass most of the cases, but few could not be passed. 
I would like to learn more about it, but due to lack of time, I switched to dfs method as I am little more familiar to this.
'''
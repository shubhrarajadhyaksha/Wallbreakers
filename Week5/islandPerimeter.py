class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n_rows=len(grid)
        n_cols=len(grid[0])
        
        def return_total(row,col):
            total=0
            neighbours=[[row-1,col],[row+1,col],[row,col-1],[row,col+1]]
            for items in neighbours:
                r,c=items
                if r in range(0,n_rows) and c in range(0,n_cols):
                    if grid[r][c]==0:
                        total+=1
                        
                else:
                    total+=1
            return total
        
        return_ans=0
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j]==1:
                    total=return_total(i,j)
                    # print(total)
                    return_ans+=total
                
        return return_ans
                
                        
            
        
        
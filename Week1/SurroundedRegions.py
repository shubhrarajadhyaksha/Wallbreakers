class Solution(object):
    def dfs(self,board,r,c):
       
        # print("r=",r)
        # print("c=",c)
        
        rows=len(board)
        cols=len(board[0])
        if r not in range(rows):
            return 
        if c not in range(cols):
            return  
        
        # print("R=",r)
        # print("C=",c)
        if board[r][c] == "." or board[r][c] == 'X':
            # print("Reached")
            return
        board[r][c] = ".";
        # print(". ", board[r][c])
        self.dfs(board, r + 1, c)
        self.dfs(board, r - 1, c)
        self.dfs(board, r, c + 1)
        self.dfs(board, r, c - 1)
        # print(board)
        
        
#         if self.dfs(board,r+1,c) and self.dfs(board,r-1,c) and self.dfs(board,r,c+1) and self.dfs(board,r,c-1):
#             board[r][c]="X"
            
#         else:
#             return False
        
        
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board!=None or len(board)!=0:
            rows=len(board)
            cols=0
            if rows>0:
                cols=len(board[0])
            
            for r in range(rows):
                for c in range(cols):
                    if board[r][c]=="O":
                        if (r==0 or r==rows-1 or c==0 or c==cols-1):
                            self.dfs(board,r,c)
                            
            for r in range(rows):
                for c in range(cols):
                    if board[r][c]==".":
                        board[r][c]="O"
                    else:
                        board[r][c]="X"
            
#Note: I tried it many times using many ways and got stuck in a loop. I will check the solution now, will try to understand and implement the same. 
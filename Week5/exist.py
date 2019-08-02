class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows=len(board)
        cols=len(board[0])
        index=0
        l=len(word)
        
        def dfs(board,r,c,i):
            if i==l:
                return True 
            if r<0 or r>=rows:
                return False
            if c<0 or c>=cols:
                return False
            
            char=board[r][c]
            if char==word[i]:
                board[r][c]="."
                
                if dfs(board,r+1,c,i+1) or dfs(board,r-1,c,i+1) or dfs(board,r,c+1,i+1)or dfs(board,r,c-1,i+1):
                    return True
                board[r][c]=char
                     
            return False
            
            
            
        for r in range(rows):
            for c in range(cols):
                if dfs(board,r,c,0):
                    return True
                
        return False
                
                
                
        
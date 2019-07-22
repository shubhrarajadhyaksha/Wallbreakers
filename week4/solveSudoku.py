class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        l=len(board)
        
        def val_adder(board,row,col):
            def is_valid(row,col,val,board):
                for i in range(l):
                    
                    if val==board[i][col]:
                        return False 
                for i in range(l):
                    if val==board[row][i]:
                        return False
                regions=int(math.sqrt(l))
                I= row//regions
                J= col//regions
                rw=regions*I
                cl=regions*J
                
                for i in range(regions):
                    for j in range(regions):
                        if val==board[rw+i][cl+j]:
                            return False
                return True 
                            
#             print("row=",row)        
#             print("col=",col)  
                
            if col==l:
                col=0
                row+=1
            
            if row==l:
                return True 
            
            if board[row][col]!='.':
                return val_adder(board,row,col+1)
            
            for i in range(1,l+1):
#                 print("row=",row)        
#                 print("col=",col) 
#                 print(i)
                val=str(i)
                if is_valid(row,col,val,board):
                    board[row][col]=val
                    if val_adder(board,row,col+1):
                        return True 
            board[row][col]='.'
            return False
                         
                    
        val_adder(board,0,0)
        
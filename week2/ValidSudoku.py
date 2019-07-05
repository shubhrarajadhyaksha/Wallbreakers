class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            s=set()
            for j in range(9):
                if board[i][j] in s:
                    # print("oh")
                    return False
                if board[i][j]!=".":
                    s.add(board[i][j])
                
        for j in range(9):
            s=set()
            for i in range(9):
                # if j==3 or j==4:
                #     print(board[i][j])
                #     print("s=",s)
                if board[i][j] in s:
                    
                    # print("my")
                    return False
                if board[i][j]!=".":
                    s.add(board[i][j])
        
        i=0
        box={}
        for i in range(9):
            for j in range(9):
                n=board[i][j]
                if n!=".":
                    b=(i//3)*3+j//3
                    if b in box:
                        if n in box[b]:
                            # print(box)
                            # print("god")
                            return False
                        box[b].append(n)
                    else:
                        box[b]=[]
                        box[b].append(n)
        
        # print(box)
        return True
                
            
            
            
                
        
        
#I just thought that there are 3 cases, The point where I was stuck was about how to find which box it belongs to ( in the third case). That was the only tricky part. 
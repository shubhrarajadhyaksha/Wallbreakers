class Node(object):
    def __init__(self):
        self.children={}
        self.end=False
        self.word=""
        
class Solution(object):
    def __init__(self):
        self.root=Node()
        # self.results=[]
        
    def create_trie(self,word):
        cur=self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter]=Node()
            cur=cur.children[letter]
        cur.end=True
        cur.word=word
        
    # def searchTrie(self,word):
    #     cur=self.root
    #     for letter in word:
    #         if letter in cur.children:
    #             cur=cur.children[letter]
    #         else:
    #             return 
    #     return cur.end,cur.word
        
        
    def dfs(self,board,row,col,r,c,cur_visit,node,res):
        # print("For row ",r," column ",c)
        # print("Current_visited",cur_visit)
        if r<0 or r>=row or c<0 or c>=col or cur_visit[r][c]==True:
            # print("Out of bound")
            return 
        # print("letter is ",board[r][c])
        
        if board[r][c] not in node.children:
            # print(board[r][c], " not in the children so return")
            return 
        this_node=node.children[board[r][c]]
        if this_node.word!="":
            # print("Word formed",node.word)
            res.append(this_node.word)
            this_node.word=""
            
        cur_visit[r][c]=True
        
        
        for next_row,next_col in (r,c+1),(r,c-1),(r-1,c),(r+1,c):
            # print("reached here")
            self.dfs(board,row,col,next_row,next_col,cur_visit,this_node,res)
        cur_visit[r][c]=False
            
        
        
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        for items in words:
            self.create_trie(items)
        
        # print(self.searchTrie("oath"))
        # print(self.searchTrie("eat"))
        # print(self.searchTrie("oathi"))
        
        row=len(board)
        col=len(board[0])
        visited=[[False for i in range(col)]for j in range(row)]
        for r in range(row):
            for c in range(col):
                cur=self.root
                self.dfs(board,row,col,r,c,visited,cur,res)
                # visited=[False for i in range(len(board)*len(board[0]))]
                # start=board[r][c]
        return(res)
                
                
            
        
        
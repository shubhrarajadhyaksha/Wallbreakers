class Trie(object):
    def __init__(self):
        self.children={}
        self.end=False
        self.word=""
class Solution(object):
    
    def __init__(self):
        self.root=Trie()
        
    
    def create_trie(self,word):
        cur=self.root
        
        for char in word:
            if char not in cur.children:
                cur.children[char]=Trie()
            cur=cur.children[char]
        cur.end=True
        cur.word=word
        
    def find_long(self):
        max_word=""
        cur=self.root
        nodes=[cur]
        
        while(nodes):
            node=nodes.pop(-1)
            
            
            if node==self.root:
                for item in node.children:
                    nodes.append(node.children[item])
            
            #not root node 
            else:
                if node.end!=False:
                    for item in node.children:
                        nodes.append(node.children[item])
                        
                    if node.word!=None:
                        word=node.word
                            # print(word)
                        if len(max_word)<len(word):
                               max_word=word
                        if len(max_word)==len(word):
                            max_word=word if word<max_word else max_word
                # print(nodes)
                
        return max_word
                    
        
        
        
#     def find_long(self):
#         lon=[]
#         max_len=0
#         max_word=""
#         cur=self.root
#         nodes=[[self.root,[]]]
        
#         while(nodes):
#             x=nodes.pop()
#             print("***")
#             print(x)
#             #root,[]
#             #[[a,[a]],[b,[b]]]
#             #x=[a,[a]]
            
#             print("X[1]=",x[1])
#             p=x[1]
#             for items in x[0].children:
#                 #a,b
#                 # print(items)
#                 l=[]
#                 l=x[1] #[]
#                 print(l)
#                 tri_node=x[0].children[items]
#                 l.append(items) #[a]
#                 print(l)
#                 nodes.append([tri_node,l])
#                 l=[]
            
#             if (x[0]!=self.root and x[0].end==True):
#                 if len(x[1])>max_len:
#                     max_len=len(x[1])
                    
#                     max_word="".join(x[1])
                    
#                 elif len(x[1])==max_len:
#                     max_word=max_word if max_word<"".join(x[1]) else "".join(x[1])
#         return max_word
                    
          
                    
                        
                
                
            
        # while(len(cur.children)<=1 ):
        #     print(cur.children)
        #     if len(cur.children)==0:
        #         return "".join(lon)
        #     item=cur.children.keys()[0]
        #     lon.append(item)
        #     cur=cur.children[item]
        
            
        
            
                
    
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for item in words:
            self.create_trie(item)
            
        lon=self.find_long()
        return(lon)
        # cur=self.root
        # print(cur.children)
        # cur=self.root
        # print(cur.children["b"].word)
#I was little confused about creating the word at the go to check the word length, but then I thouhgt of adding it to the node. 
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        matrix=[[None for i in range(len(word1)+1)] for j in range(len(word2)+1)]
        # print(matrix)
        #i for word2 j for word1
        n=0
        for i in range(0,len(matrix)):
            matrix[i][0]=n
            n+=1
        n=0    
        for j in range(0,len(matrix[0])):
            matrix[0][j]=n
            n+=1
            
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                # print(i,j)
                # print("word2",word2[i])
                # print("word1",word1[j])
                if word2[i-1]==word1[j-1]:
                    matrix[i][j]=matrix[i-1][j-1]
                    
                else:
                    matrix[i][j]=1+min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1])
                    
        return(matrix[-1][-1])
            
        
        
        
        
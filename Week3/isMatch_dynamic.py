class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #2D matrix with number of rows=s length and number of cols=p length
        matrix=[[False for i in range(len(p)+1)]for j in range (len(s)+1)]
        
        matrix[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=="*":
                matrix[0][i]=matrix[0][i-2]
        
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if p[j-1]==s[i-1] or p[j-1]==".":
                    matrix[i][j]=matrix[i-1][j-1]
                    
                elif p[j-1]=="*":
                    matrix[i][j]=matrix[i][j-2]
                    if s[i-1]==p[j-2] or p[j-2]==".":
                        matrix[i][j]=matrix[i][j] or matrix[i-1][j]
                        
                else:
                    matrix[i][j]=False
                    
        return(matrix[-1][-1])
                    
                
        
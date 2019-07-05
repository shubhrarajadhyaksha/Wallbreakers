class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        answer={}
        
        def dic(answer,sentence):
            s=sentence.split()
            for item in s:
                if not item in answer:
                    answer[item]=1

                else:
                    answer[item]+=1
                    
        dic(answer,A)
        dic(answer,B)
        
        final_answer=[]
        
        for item in answer:
            if answer[item]==1:
                final_answer.append(item)
        
        return final_answer

# Using hashmap was the first thing which came to my mind
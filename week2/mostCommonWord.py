import collections
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        replace="!?',;."
        for letter in paragraph:
            if letter in replace:
                paragraph=paragraph.replace(letter," ")
                
        paragraph=paragraph.lower().split()
        ans=collections.Counter()
        max_len=0
        max_word=""
        for word in paragraph:
            if word not in banned:
                ans[word]+=1
                if  ans[word]>max_len:
                    max_len= ans[word]
                    max_word=word
        return max_word
                
        
#         replace="!?',;."
#         for letter in paragraph:
#             if letter in replace:
#                 paragraph=paragraph.replace(letter," ")
                
#         paragraph=paragraph.lower().split()
#         print(paragraph)
#         dic={}
#         m=0
#         val=""
#         for item in paragraph:
#             if item not in banned:
#                 if item not in dic:
#                     dic[item]=1
#                 else:
#                     dic[item]+=1
#                 if dic[item]>m:
#                     m=dic[item]
#                     val=item
#         return val
                    
        
        
        
        
#         dic={}
#         maximum=0
#         paragraph=paragraph.translate(string.punctuation)
#         paragraph=paragraph.replace("!"," ")
#         paragraph=paragraph.replace("?"," ")
#         paragraph=paragraph.replace("''"," ")
#         paragraph=paragraph.replace(","," ")
#         paragraph=paragraph.replace(";"," ")
#         paragraph=paragraph.replace("."," ")
#         para=paragraph.lower().split()
#         # return_list=[]
#         for item in para:
#             if item not in banned:
#                 # print(item)
#                 if item not in dic:
#                     dic[item]=1
#                 else:
#                     dic[item]+=1
#                 # if dic[item]==maximum:
#                 #     return_list.append(item)
                
#                 if dic[item]>maximum:
#                     maximum=dic[item]
#                     # return_list=[]
#                     # return_list.append(item)
#         # print(dic)
#         for item,val in dic.iteritems():
#             if val==maximum:
#                 return item
        
                
        
        
            
        
import collections
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        multiset=collections.Counter()
        for items in A:
            even=collections.Counter()
            odd=collections.Counter()
            for index,value in enumerate(items):
                if index%2==0:
                    even[value]+=1
                else:
                    odd[value]+=1
                
            multiset[items]=dict()
            multiset[items].update({'even':even, 'odd':odd})
            
        lis=[]
        for item in multiset:
            if multiset[item] not in lis:
                lis.append(multiset[item])
                    
        # print(multiset)
        # print(lis)
        return len(lis)
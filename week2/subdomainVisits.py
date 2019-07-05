import collections
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # print(cpdomains)
        ans=collections.Counter()
        for item in cpdomains:
            # print(item)
            number,url=item.split()
            # print(number)
            # print(url)
            
            parts_multiple=url.split(".")
            l=len(parts_multiple)
            
            for i in range(l):
                ans[".".join(parts_multiple[i:])]+=int(number)
                
        a=[]
        for key,val in ans.items():
            b=str(val)+" "+str(key)
            a.append(b)
            
        return (a)
            
            
        
import bisect 
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #s if the complete string 
        #p is the string to be found 
        def binary_search(start,end,array,target):
            while start<=end:
                # print(start,end)
                mid=(start+end)//2
                # print(mid)
                if array[mid]==target:
                    return mid

                if array[mid]>target:
                    end=mid-1

                elif array[mid]<target:
                    start=mid+1
                    
        if len(s)<len(p):
            return []
        if not p or not s:
            return []
        output=[]
        items=set(p)
        p=sorted(p)
        l_p=len(p)
        l_s=len(s)
        
        check=sorted(s[0:l_p])
        if p==check:
            output.append(0)
            
        for i in range(1,l_s-l_p+1):
            # print(check)
            r_item=s[i-1]
            a_item=s[i+l_p-1]
            #remove r_item from current sorted list 
            #search for item using binary search
            #and add item a_item at correct place
            #item can be added using bisect 
            r_item_from=binary_search(0,l_p-1,check,r_item)
            check.pop(r_item_from)
            
            insert_to=bisect.bisect(check, a_item)
            check.insert(insert_to, a_item)
            # print(r_item,a_item,r_item_from,check,insert_to)
            if p==check:
                output.append(i)
        return(output)
            
            
            
            
            
        
        
        
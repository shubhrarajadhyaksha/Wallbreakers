class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        def get_num(index):
            if index>=len(formula):
                return 1,0
            if formula[index].isalpha() or formula[index] in ["(",")"] :
                return 1,0
            else:
                start=index
                end=index+1
                while (index<len(formula) and formula[index].isdigit()):
                    index+=1
                    end=index
                    
                return int(formula[start:end]),len(formula[start:end])
                    
            
        def get_element_and_atoms(index):
            # print("The index is",index)
            if formula[index].isalpha():
                start=index
                end=index+1
                index+=1
                while(index<len(formula) and formula[index].isalpha() and formula[index].islower()):
                    index+=1
                    end=index
                
                element=formula[start:end]
                number,length=get_num(end)
            
                total_length=length+len(element)
                # print("element ",element," ","number",number,"length",total_length)
                return element,number,total_length
                
        i=0     
        stack=[]
        while(i<len(formula)):
            # print(i)
            if formula[i]=="(":
                stack.append("(")
                i+=1
                
            elif formula[i].isalpha():
                element,number,length=get_element_and_atoms(i)
                # print(element)
                # print(number)
                # print(length)
                stack.append([element,number])
                i+=length
                
            elif formula[i].isdigit():
                number,length=get_num(i)
                lis=[]
                # print(stack)
                stack.pop(-1)
                # print(stack)
                item=stack.pop(-1)
                # print(stack)
                
                while(item!="("):
                    # print(item)
                    lis.append([item[0],item[1]*number])
                    item=stack.pop(-1)
                    
                for items in lis:
                    stack.append(items)
                
                
                # stack.append(number)
                i+=length
                
            elif formula[i]==")":
                stack.append(")")
                i+=1
        
        # print(stack)
        hashmap=collections.Counter()
        while(stack):
            item=stack.pop()
            # print(item)
            hashmap[item[0]]+=item[1]
            
        x = sorted(hashmap.items(), key=lambda kv: kv[0])
        lis=[]
        for items in x:
            if items[1]==1:
                st=str(items[0])
            else:
                st=str(items[0])+str(items[1])
            lis.append(st)
            
        return "".join(lis)
            
        
        # print(hashmap)
            
                
                
            
            
                    
            
                    
        
        
        
class dnode:
    def __init__(self,key=None,val=None):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.head=dnode()
        self.tail=dnode()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.hashmap={}
        self.capacity=capacity
        self.items_present=0 
        
        
    def check_item(self,key):
        if key in self.hashmap:
            return True
        return False 
    
    def create_node(self,key,value):
        node=dnode(key,value)
        # print(" Creating new node")
        # print("key is ",key)
        # print("value is ",value)
        # print(node.key)
        # print(node.val)
        return node 
    
    def get_node(self,key):
        return self.hashmap[key]
    
    def delete_node(self,key):
        del self.hashmap[key]
    
    def add_node_front(self,node):
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
        node.prev=self.head
        
    def remove_node(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev
        # self.delete_node(node.key)
    
    def remove_extra_node(self):
        node=self.tail.prev
        node.prev.next=self.tail
        self.tail.prev=node.prev
        self.delete_node(node.key)
        
    def update_hashmap_value(self,key,new_node):
        self.hashmap[key]=new_node
    
    # def printll(self,head):
    #     print(" The linkedlist is ")
    #     while head!=self.tail:
    #         print(head.key,head.val)
    #         head=head.next
    #     print(" The hashmap is ")
    #     for items in self.hashmap:
    #         print(items,self.hashmap[items].val)
        
        

    def get(self, key: int) -> int:
        # print("get key",key)
        if not self.check_item(key):
            return -1
        node=self.get_node(key)
        value=node.val
        self.remove_node(node)
        self.add_node_front(node)
        # cur=self.head.next
        # self.printll(cur)
        return value
        
        
        
        

    def put(self, key: int, value: int) -> None:
        # print("put key",key, " value ",value)
        # print(key)
        # print(value)
        node=self.create_node(key,value)
        if self.check_item(key):
            curr_node=self.get_node(key)
            self.update_hashmap_value(key,node)
            self.remove_node(curr_node)
            self.add_node_front(node)
        elif self.capacity>self.items_present:
            self.items_present+=1
            self.add_node_front(node)
            self.hashmap[key]=node
            
        else:
            self.remove_extra_node()
            self.add_node_front(node)
            self.hashmap[key]=node
            
        # cur=self.head.next
        # self.printll(cur)
            
            
            
            
            
            
            
            
            
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
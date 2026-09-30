class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
    def insert(self,data):
        n=Node(data)
        if self.head == None:
            self.head=n
            return
        t=self.head    
        while t.next:
            t=t.next
        t.next=n
    def res(self):
        t=self.head
        while t!=None:
            print(t.data,end='->')
            t=t.next
obj=LL()     
obj.insert(40) 
obj.insert(30)                         
obj.insert(20)   
obj.insert(10)   
obj.res()
print("NONE")                                    
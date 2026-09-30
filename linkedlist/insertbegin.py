class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class INSERT:
    def __init__(self):
        self.head=None
    def insertAtbegin(self,data):
        n=Node(data) # ip 10: -create node -------#ip20: create node
        n.next=self.head # [10 | None]-------#[20| head=10 ]--[20|10]
        self.head=n #head=10 new head=20
    def res(self):
        t=self.head
        while t:
            print(t.data,end=" ")
            t=t.next
obj=INSERT()     
obj.insertAtbegin(10) 
obj.insertAtbegin(20)                         
obj.insertAtbegin(30)   
obj.insertAtbegin(40)   
obj.res()
print("NONE")
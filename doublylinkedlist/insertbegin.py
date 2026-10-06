class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.pre=None
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def Insert(self,d):
        n=Node(d)
        if self.head==None:
            self.head=n
            self.tail=n
            return
        n.next=self.head
        self.head.pre=n
        self.head=n
    def Res(self):
        t=self.head
        while t:
            print(t.data,end=" ")
            t=t.next
obj=DLL()
obj.Insert(3)
obj.Insert(2)
obj.Insert(1)
obj.Insert(0)
obj.Res()             
               
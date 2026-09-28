n=int(input())
a=list(map(int,input().split()))
#method 1 
b=[]
for i in a:
    if i == 0:
        b.append(i)
for i in b:
    a.remove(i)               
print(b+a) 

      
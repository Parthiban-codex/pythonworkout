# max/min in array
a=[1,3,4,6,7,8,12]
max=a[0]
min=a[0]
for i in a:
    if i > max:
        max=i
    elif i < min:
        min=i
print(max)
print(min)        

"""--------------------------------------------------------"""
#reverse array
a=[1,2,3,4,5] 
ra=[]
for i in a[::-1]:
    ra.append(i)
print(ra)
    

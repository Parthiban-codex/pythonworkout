s=list(map(int,input().split()))
# ss=[i for i in s if i!=0]
# z=[0]*s.count(0)
# print(z+ss)
# #-----------------------------------
# sss=[]
# for i in s:
#     if i == 0:
#         sss.append(i)
#         s.remove(i)
# print(sss+s)        
#-----------------------------------------
for i in s:
    if i!=0:  
        print(i ,end=" ")
print(*[0]*s.count(0))        
        

        


        
        


issorted=True
n=int(input())
List=list(map(int,input().split()))
for i in range(len(List)-1):
    if List[i]>List[i+1]:issorted=False
 
print("sorted") if issorted else print("unsorted")

       


s=list(map(int,input().split()))
k=int(input())
if k<=len(s):
    print(s[k::]+s[:k:])
else:
    print("error")

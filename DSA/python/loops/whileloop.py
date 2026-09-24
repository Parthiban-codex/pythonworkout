#digit count
n=int(input())
temp=n
d=0
while n>0:
    d+=1
    n=n//10 #reduce number
print(f"digit count: {d}")    

#sum of digit
Sum=0
while temp>0:
    s=temp%10
    Sum+=s
    temp=temp//10
print(f"sum of digit: {Sum}")    

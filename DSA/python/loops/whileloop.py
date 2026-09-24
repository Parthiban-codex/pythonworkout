
#digit count
n=int(input())
temp,val=n,n
d=0
while n>0:
    d+=1
    n=n//10 #reduce number
print(f"digit count: {d}")    

#sum of digit
Sum=0
while temp>0:
    s=temp%10 #mod-get last value
    Sum+=s
    temp=temp//10 #div-cutoff last value
print(f"sum of digit: {Sum}")  

#product of digit
pro=1
while val>0:
    pro*=val%10
    val=val//10
print(f"product of digit: {pro}")    
    
n=int(input())
rev=0
while n>0: #123>0 t
    v=n%10 #get last digit by (%) #123 % 10 = 3 
    rev=rev*10+v #0 * 10 = 0 + 3
    n=n//10 #remove last digit by (//) # n=123//10 = 12
print(rev)    
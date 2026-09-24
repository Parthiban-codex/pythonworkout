#divisible by 4 and not divisible by 100
#if divisible by 100 also divisible bt 400
year=int(input())
if year%4==0 and year%100!=0 or year%400==0:
    print("leap year")
else:
    print(" not leap year")
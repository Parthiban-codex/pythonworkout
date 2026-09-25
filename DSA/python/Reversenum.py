n=int(input())
rev=0
while n>0: #123>0 T
    v=n%10 #get last digit by (%) #123 % 10 = 3 
    rev=rev*10+v #0 * 10 = 0 + 3
    n=n//10 #remove last digit by (//) # n=123//10 = 12
print(rev)  

#reverse in oop
class reverse(): 
    rev_digit=0  
    def rev(self):
        num=int(input())
        
        while num>0:
            last_digit=n%10
            rev_digit=rev_digit*10+last_digit
            num=num//10
        print(f"reversed digit: {rev_digit}") 
obj=reverse()
obj.rev() 


        
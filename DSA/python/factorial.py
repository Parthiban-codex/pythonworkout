#factorial 
n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact) 

class Fact():

    def factorial(self):
        f=1
        for i in range(1,n+1):
            f=f*i
        print(f" factorial of given num: {f}")    
obj=Fact()
obj.factorial()        

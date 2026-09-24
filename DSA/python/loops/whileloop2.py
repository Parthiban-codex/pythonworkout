class While():
    n=int(input())
    temp1,temp2=n,n
    def sum_ofdigit(self):
        Sum=0
        while n>0:
            Sum+=n%10 
            n=n//10
        print(f"sum of digit: {Sum}")
    def DC(self):
        Count=0
        while temp1>0:
            Count+=1
            temp1=temp1//10
        print(f"digit count: {Count}")
    def pro_ofdigit(self):
        pro=1
        while temp2>0:
            pro*=temp2%10 
            temp2=temp2//10
        print(f"product of digit: {pro}")      
obj=While()
obj.sum_ofdigit()
obj.pro_ofdigit()
obj.DC()             
            
            
class prime():
    def prime_number(self):
        number=int(input("give num: "))

        if number<=1:
            return "not a prime"
        for i in range(2,number//2):
            if number % i == 0:
                return "not a prime"
        return "prime number"   


obj=prime()
print(obj.prime_number())
            
           
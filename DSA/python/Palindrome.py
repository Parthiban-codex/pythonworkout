class Palindrome:
    def letter(self):
        word=input()
        word=list(word)
        nword=[]
        for i in word[::-1]:
            nword.append(i)
            
    
        if word == nword:
            print("palidrome")
        else: 
            print("not a palindrome")  
obj=Palindrome()
obj.letter()              

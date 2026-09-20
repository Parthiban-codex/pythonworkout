class space():
    def space(self):
        word=input("enter word1 ")
        nword=[]
        for i in list(word):
            if i==" ":
                continue
            else:
                nword.append(i)
        nword="".join(nword)  
        print(nword)
obj=space()
obj.space()        


#method2
a=input("enter word2 ")
for i in a:
    if i ==" ":
        continue
    else:
        print(i,end="")    
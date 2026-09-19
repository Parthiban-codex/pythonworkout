class COUNT():
    def SC(self):
        sentence="the python is a  programming    "
        sentence=sentence.split()
        print(f"sentence count : {len(sentence)}")
    def LC(self):
        letter="the python is super  language        "    
        letter=list(letter)
        lcount=0
        for i in letter:
            if i==" ":
                continue
            else:
                lcount+=1
        print(f"letter count: {lcount}")      
obj=COUNT()
obj.SC()
obj.LC()        
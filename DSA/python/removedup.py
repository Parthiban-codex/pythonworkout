class dup():
    def rm(self):
        string=input(" ")
        string2=" "
        for i in string:
            if i not in string2:
                string2+=i
            else:
                pass
        print(f"old str: {string}")
        print(F"new str: {string2}")
obj=dup()
obj.rm()               

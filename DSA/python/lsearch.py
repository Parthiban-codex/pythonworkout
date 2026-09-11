#linear search
class ls():
    def search(self):
        b = [15, 45, 67, 8, 3, 123, 9, 'string',None,"apple",True]
        key = True
        for i in b:
            if i == key:
                print("key found", i)
                break
        else:
            print("not found")


obj=ls()
obj.search()
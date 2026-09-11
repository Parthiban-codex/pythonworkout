class ANAGRAM():
    def anagram(self):
        a = ("owv")
        b = "now"
        a = list(sorted(a))
        b = list(sorted(b))
        print(f"list of a: {a}")
        print(f"list of b: {b}")
        if a == b:
            print("anagram")
        else:
            print("not a anagram")
obj=ANAGRAM()
obj.anagram()





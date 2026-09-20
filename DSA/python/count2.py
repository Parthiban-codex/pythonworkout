class character():    
    def func(self):
        words=0
        digits=0
        spaces=0
        others=0
        inputt=input(" ")

      
        for i in inputt:
            if ("a" <= i <= "z" )or ("A" <= i <= "Z"):
                words +=1
            elif ("0" <= i <= "9"): 
                digits +=1 
            elif (i == " "):
                spaces +=1
            else:
                others +=1
        return f"Letters: {words} \nDigits: {digits} \nSpaces: {spaces} \nSpecial: {others}"

obj = character()
print(obj.func())                    

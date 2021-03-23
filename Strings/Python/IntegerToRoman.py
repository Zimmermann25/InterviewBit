class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        
        if A<1 or A >3999:return None
        output = ""
        
        while A>= 1000:
            A-=1000
            output += "M"
        
        # tutaj A max 999, najpierw kombinacja CM
        if A>=900:
            output += "CM"
            A -= 900
        else: # pomiedzy 500 i 900
            if A>=500:
                output += "D"
                A -= 500
                while A>=600:
                    A-=100
                    output += "C"
            
                
        #print("after D A: ", A)

        if A >=400:     # opcja CD
            output += "CD"
            A -= 400
        else:
            while A>=100: # pomiedzy 100 i 400
                output += "C"
                A -= 100
            
        #tutaj max 99
        if A >=90:
            A -= 90
            output += "XC"
        else:
            if A >=50:
                output += "L"
                A -= 50
                while A >=10:
                    A-=10
                    output += "X"
        
        # max 50
        if A >=40:
            A -=40
            output += "XL"
        else:
            while A>=10: # pomiedzy 100 i 400
                output += "X"
                A -= 10
                
        
        # max 10
        if A >=9:
            output += "IX"
            A -= 9
        else:
            if A >= 5:
                A -= 5
                output += "V"
                while A >=1:
                    A -=1
                    output += "I"
            
        # max 5 tutaj
        if A>=4:
            output += "IV"
            A -= 4
        else:
            while A >=1:
                output += "I"
                A -=1
     
                
        #print("A zostalo: ", A)
        
        return output
    
        
        
        
        
        
        
        
        

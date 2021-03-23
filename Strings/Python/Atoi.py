class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        # zero z lewej moze byc
        #zle znaki z lewej dyskwalfikują całkowicie
        c = 0
        newA = ""
        firstNumFound = False
        A.strip()
        sign = 1
        signFound = False
        while c < len(A):
            # jesli zle znaki z 
            if ord(A[c]) == 45 and signFound==False:
                sign = -1
                c+=1
                signFound = True
            elif ord(A[c]) == 43:
                sign = 1
                c +=1 # przejdz dalej
                signFound = True
                
            if A[c] == " " or ord(A[c]) < 48 or ord(A[c]) > 57 :
                break
            else:
                newA += A[c]
                signFound = True # jesli pasuje liczba, to jakis znak jest znany
            c +=1
        
        number = 0
        
        i = len(newA)-1
        base = 1
        while i >=0:
            #print(ord(newA[i]), "num: ", number)
            number += (ord(newA[i]) - 48) * base
        
            i-=1
            base*=10
        
        number *=sign
        if number > 2**31 - 1:
            return 2**31 - 1
        elif number < -2**31:
            return -2**31
        
        return number
                
        
        

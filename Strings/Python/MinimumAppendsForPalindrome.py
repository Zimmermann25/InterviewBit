class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if len(A) <2:return 0
        
        # jak jest juz palindromem, to zero
        left= 0
        right = len(A)-1
        isValid = True
        while left <= right:
            #print("left: ", tempStr[left], "right: ", tempStr[right])
            if A[left] != A[right]:
                isValid = False
                break
            left +=1
            right -=1
        if isValid:return 0
        
        # fajne rozwiązanie od Ritik_Arora , myślałem o czymś podobnym, ale odrzuciłem
        # ten pomysł, a szkoda
        #EDIT, jednak nie działa dobrze, babb exc 1 out 2
        
        left = 0
        right = len(A)-1
        counter = 0
        while left <=right:
            if A[left] == A[right]:
                left +=1
                right -=1
            else: # jak są różne, to przesuwaj tylko lewy wskażnik
                left +=1
                counter += (len(A)-right)
                right = len(A)-1 # ostatni znak z A, right normalnie się zmniejsza 
                # jesli takie same jak A[left]
        
        return counter
        
        #TLE
        '''i = 0 # indeks przedostatniego znaku
        charArr = [A[i] for i in range(len(A))]
        counter = 0
        
        # bez ostatniego znaku z A
        reverse = [A[i] for i in range(len(A)-2, -1, -1)]
        #print("reverse: ", reverse)
        while i < len(A):
            isValid = True
            tempStr = A
            j=len(reverse)-i-1 # od ktorego indeksu z reverse zacząć przyłączanie
            #print("j: ", j, "i: ", i)
            while j <len(reverse): # od pozycji reverse[j] do końca reverse dołączaj
                tempStr += reverse[j]
                j+=1
            
            # sprawdzenie czy palindrom
            left= 0
            right = len(tempStr)-1
            #print("tempStr: ", tempStr)
            while left <= right:
                #print("left: ", tempStr[left], "right: ", tempStr[right])
                if tempStr[left] != tempStr[right]:
                    isValid = False
                    break
                
                left +=1
                right -=1

            if isValid:return i+1
            i+=1
     
        return len(A)-1 # worst case'''
            
            
            
            
        
        

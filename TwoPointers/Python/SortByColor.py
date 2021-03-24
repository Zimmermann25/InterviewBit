class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        # można też przerzucić poprzez zamianę, 0 na początek, a 2 na koniec, wtedy
        #1 będą po środku na poprawnych pozycjach
        zerosCounter = 0
        onesCounter = 0
        twosCounter = 0
        
        for i in range(len(A)):
            if A[i]==0:zerosCounter +=1
            if A[i]==1:onesCounter +=1
            if A[i]==2:twosCounter +=1
        
        for i in range(zerosCounter):
            A[i] = 0
        
        for i in range(onesCounter):
            A[i+zerosCounter] = 1
        
        for i in range(twosCounter):
            A[i+zerosCounter + onesCounter] = 2
            
            
        return A
        

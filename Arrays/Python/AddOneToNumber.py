class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        #obciecie zer z lewej
        counter = 0
        while counter < len(A) and len(A) > 1:
            if A[0] == 0:
                del A[0]
            else:break
            counter += 1
            
        lastIndex = len(A) - 1
        while lastIndex >=0:
            if A[lastIndex] == 9:
                lastIndex-=1
            else:
                A[lastIndex] += 1
                break
            
        #przypadek typu 21999
        #print(lastIndex)
        if(lastIndex >=0):
            for i in range(lastIndex+1, len(A)):
                A[i] = 0
                
         #przypadek typu 999, gdzie trzeba zwiekszyc rozmiar tablicy
        if(lastIndex <0):
            A.insert(0,1)
            for i in range(1, len(A)):
                A[i] = 0
        return A 
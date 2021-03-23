class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        occur = []
        for i in range(len(A)):
            occur.append(0)
        #print(occur)
        for i in range(len(A)):
            # normalnie tutaj sprawdzenie wartosci by bylo, ale jest zalozenie 1 do n
            occur[A[i]-1] += 1
            if occur[A[i]-1] >1:
                return A[i]
        
        return -1 # nie znaleziono duplikatow
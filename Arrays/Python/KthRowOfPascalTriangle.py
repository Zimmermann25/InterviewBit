class Solution:
    # @param A : integer
    # @return a list of integers
    
        
    def getRow(self, A):
        def factorial(n):
            nFac = 1
            for i in range(1, n+1):
                nFac *= i
            return nFac
        
        def newtonBinomial(n, k):
            return int(factorial(n) / (factorial(n-k) * factorial(k)))
        
        # dwumian newtona
        
        outputArr = [1] * (A+1)
        for k in range(1, A):
            outputArr[k] = newtonBinomial(A, k)
        return outputArr
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, a, b):  
        if a == 0 : 
            return b  
        return self.gcd(b%a, a) 
    
    def cpFact(self, A, B):
        if A==1:return 1
        
        while self.gcd(A, B)!=1:
            A //= self.gcd(A, B)
        
        
        
        return A # jeśli nic nie znajdzie w przedziale do A
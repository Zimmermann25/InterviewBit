class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        #distinct integers, więc moge tak
        hash = set()
        counter = 0
        for i in range(len(A)):
            
            if A[i] ^ B in hash:
                counter +=1 
            hash.add(A[i])
        
        return counter
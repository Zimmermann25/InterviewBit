class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        
        mask = 1
        for i in range(32):
            
            if A & mask:
                return i
            
            mask <<=1
        
        return 32 # same zera
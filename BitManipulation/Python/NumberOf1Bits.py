class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        
        mask = 1
        counter = 0
        '''for i in range(32):
            if A & mask:
                counter +=1
            mask <<=1'''
        
        while A!=0:
            A = A&(A-1)
            counter +=1
        
        return counter
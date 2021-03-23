import math
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        #print(math.ceil(math.sqrt(A)))
        for i in range(1, math.ceil(math.sqrt(A))+1):
            base = i
            power = 2
            number = 1
            while base ** power <= A:
                if base ** power == A:
                    return 1
                power+=1
        return 0
        
        
        

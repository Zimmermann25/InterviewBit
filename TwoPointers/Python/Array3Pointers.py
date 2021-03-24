class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        
        if len(A)==len(B)==len(C)==0:return 2147483647
        if len(A) < 1 or len(B) < 1 or len(C) < 1:return 2147483647
        
        i = 0
        j = 0
        k = 0
        out = max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
        inci = False
        inck = False
        incj = False
        
        while i < len(A) and j < len(B) and k < len(C):
            temp = max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
            
            # find cur smallest elem from 3 arrays
            curSmallest = A[i]
            inci = True
            incj = inck = False
            if B[j] < curSmallest:
                curSmallest = B[j]
                inci = inck = False
                incj = True
            if C[k] < curSmallest:
                curSmallest = C[k]
                inci = incj = False
                inck = True
            
            if inci: i += 1
            if incj: j +=1
            if inck: k +=1
                    
            
            if temp < out:
                out = temp
        
        
        return out
        
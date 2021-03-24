class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        counterA = 0
        counterB = 0
        output = []
        while counterA + counterB < len(A) + len(B):
            if counterA< len(A): Aval = A[counterA]
            else:break
            
            if counterB< len(B): Bval = B[counterB]
            else:break
            
            if Aval < Bval: counterA +=1
            elif Aval==Bval:
                output.append(Aval)
                counterB+=1
                counterA += 1
            else: counterB+=1
        
        return output
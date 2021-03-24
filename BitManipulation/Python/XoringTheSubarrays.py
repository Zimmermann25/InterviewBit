class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) < 1 or len(A) % 2==0:return 0
        
        output = 0
        #dla parzystej dlugości xory się zneutralizują, dla nieparzystych
        # co druga wartość zostanie
        for i in range(0, len(A), 2):
            #howMany = (i+1) * (len(A)-i)
            #if howMany % 2 != 0:
            output = output ^ A[i]
            #print("out: ", output, "A[i]: ", A[i])
            
            
            
        return output
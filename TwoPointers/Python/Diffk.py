class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        
        if len(A) < 1: return 0
        
        i = 0
        j = 1 # A[j] > A[i], A[j] - A[i] == B
        while i < len(A) and j < len(A):
            if i != j:
                diff = A[j] - A[i]
                #print(A[i], A[j], diff)
                if diff==B:
                    return 1
                elif diff < B:
                    j += 1
                elif diff > B:
                    i += 1
            else: j+=1

        
        return 0
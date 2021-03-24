class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):

        
        i = 0
        j = 0 # licznik elementow != B
        while i < len(A) and j < len(A):
            if A[i] != B:
                A[j] = A[i]
                j += 1 # znaleziono wystapienie poprawnej
            i += 1
        return j
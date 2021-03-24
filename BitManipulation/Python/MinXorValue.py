class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        
        #A.sort(key=lambda x: format(x, '017b'))
        A.sort()
        min = A[0] ^ A[1]
        for i in range(1, len(A)-1):
            if A[i] ^ A[i+1] < min:
                min = A[i] ^ A[i+1]
            #print(format(A[i], '017b'))

        return min
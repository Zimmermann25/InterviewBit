class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        counter = 0
        if(len(A)==1 and len(B)==1):
            return 0
        for i in range(len(A)-1):
            diffX = A[i+1] - A[i]
            diffY = B[i+1] - B[i]
            bigger = diffX
            if diffX < diffY: bigger = diffY
            counter += abs(bigger)
            print(counter)
        return counter    
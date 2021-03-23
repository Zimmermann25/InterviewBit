class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        max = A[0]
        min = A[0]
        for i in range(1, len(A)):
            if A[i] < min:
                min = A[i]
            if A[i] > max:
                max = A[i]
        return max + min
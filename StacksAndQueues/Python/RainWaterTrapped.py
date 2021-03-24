class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        if len(A)<3:return 0

        left = 0
        right = len(A)-1
        output = 0
        lmax = A[0]
        rmax = A[-1]
        while left <= right:
            lmax = max(A[left], lmax)
            rmax = max(A[right], rmax)
            
            if lmax <=rmax:
                output += (lmax - A[left])
                left +=1
            elif rmax <=lmax:
                output += (rmax - A[right])
                right -=1
            
        return output
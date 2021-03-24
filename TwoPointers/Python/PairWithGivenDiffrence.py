class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if len(A) < 1:return 0
        A.sort()
        
        left = 0
        right = 1
        diff = 0
        while  left < len(A) and right < len(A):
            diff = A[right] - A[left]
            #print(left, right)
            if diff ==B and left !=right:
                return 1
            elif diff <B:
                right +=1
            else:
                left +=1
        
        return 0
            
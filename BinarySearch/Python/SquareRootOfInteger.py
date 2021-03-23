class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        
        '''lower = 0
        upper = 0
        for i in range(1, A+1):
            if i*i < A:
                lower = i
            if i*i == A:
                return i
            if i*i > A:
                return lower'''
        
        low = 0
        high = A
        while low <= high:
            mid = low + int((high-low)/2)
            #print(low, mid, high)
            if mid*mid < A:
                low = mid+1
            elif mid*mid == A:
                return mid
            elif mid*mid > A:
                high = mid-1
            
            
        
            
        return low-1
        
        
        
        

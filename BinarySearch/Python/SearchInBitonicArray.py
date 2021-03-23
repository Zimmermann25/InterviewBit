class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        #caveat - first strictly increasing then after a point strictly decreasing
        # znalezc maks Elem, ktory wyznaczy granicę
        #distinct - bez powtórzeń
        
        #if len(A) < 3:return []
        halfIndex = 0
        curMax = A[0]
        for i in range(len(A)):
            if A[i] > curMax:
                curMax = A[i]
                halfIndex = i
        
        
        # od lewej do halfIndex szukanie
        left = 0
        right = halfIndex
        
        while left <= right:
            mid = (left + right)//2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                left = mid+1
            else:
                right = mid -1
        
        left = halfIndex
        right = len(A)-1
        
        while left <= right:
            mid = (left + right)//2
            if A[mid] == B:
                return mid
            elif A[mid] > B: # ponieważ tutaj jest tablica malejąca
                left = mid+1
            else:
                right = mid -1
        
        return -1
        
        
        
        


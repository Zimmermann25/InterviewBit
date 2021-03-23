class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        if len(A) < 1:return 0
        low = 0
        high = len(A)-1
        while low <= high:
            mid = (low + high)//2
            if A[mid] == B:
                return mid # jak znajdzei wystąpienie
            elif A[mid] < B:
                low = mid+1
            else:
                high = mid -1
        
        return low # jak nie znajdzie wystąpienia
        
        
        
        

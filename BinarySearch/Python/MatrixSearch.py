class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        
        low = 0
        high = (len(A) * len(A[0])) -1 
        
        while low <=high:
            mid = (low + high)//2
            curRow = mid//len(A[0])
            curCol = (mid) % len(A[0]) # tutaj niedopatrzenie byłow
            #print("curCol: ", curCol, "curRow: ", curRow, " mid: ", mid)
            if A[curRow][curCol] == B:
                return 1
            elif A[curRow][curCol] < B:
                low = mid+1
            else:
                high = mid-1
                
        return 0 
        
        

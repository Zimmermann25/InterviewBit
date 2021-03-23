class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        # transpose
        for i in range(len(A)): # row
            # swap elementow
            for j in range(i, len(A)):
                #print("i: ", i, "j: ", j)
                curRowElem = A[i][j]
                curColElem = A[j][i]
                #print(curRowElem, curColElem)
                A[i][j], A[j][i] = A[j][i], A[i][j]
                #swap
                #curRowElem, curColElem = curColElem, curRowElem
                #print(A)
        
        # zamiana w wierszach
        for i in range(len(A)):
            A[i] = A[i][::-1]
            
        return  A 
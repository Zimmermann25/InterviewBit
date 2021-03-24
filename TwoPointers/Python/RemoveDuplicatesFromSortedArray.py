class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        
        count = 0
        n = len(A)
        i = 0
        count = 0
        #print("-----")
        while i < len(A):
            #print(i, count, A)
            ommitIncrease = False
            if i < len(A)-1 and A[i] ==A[i+1]:
                i += 1
                ommitIncrease = True
            else:
                A[count] = A[i]
                count += 1
                
            if not ommitIncrease:
                i += 1
                
        return count 
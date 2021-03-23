class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, A):
        if A <1: return []
        output = [[] for i in range(A)] # base case
        output[0].append(1)
        for i in range(1, A):
            j = 1
            output[i].append(1)# zawsze
            while j <= (i-1):
                output[i].append(output[i-1][j-1] + output[i-1][j])
                j+=1
            output[i].append(1) #zawsze
        return output
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    def uniquePaths(self, A, B):
		#dynamic programming
        if(A==1):
            return 1
        Ans=[1]*B
        for i in range(1,A):
            for j in range(1,B):
                Ans[j]+=Ans[j-1]
            #print(Ans)
        return Ans[-1]
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        
        #A^B^C^D^C^A^D = B
        ans = 0;
        for i in range(len(A)):
            #print(ans)
            ans = ans^A[i];
        return ans;
        
        '''output = 0
        for i in range(0, 32):
            sm = 0
            
            mask = (1<<i)
            
            for k in range(len(A)):
                #print(k, "if: ", A[k] & mask)
                if A[k] & mask:
                    sm += 1
            if sm % 2 : # nieparzysta ilosc oznacza, ze bit z 1 jest w output
                output = output | mask
            #print(output)
        return output'''



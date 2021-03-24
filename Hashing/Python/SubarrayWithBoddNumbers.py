class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    #niesamodzielne
    def solve(self, A, B):
        for i in range(len(A)):
            if A[i] % 2==0:A[i] = 0
            else:A[i] = 1
        
        # find all subarrays with given sum
        output = 0
        countPref = {}
        prefix = 0 # prefix to cummulative sum
        countPref[prefix] =1 #dla przypadku np. (3+4) - 7 , B = 7
        for i in range(len(A)):
            #print(countPref)
            #print()
            prefix += A[i]
            expected = prefix - B
            if countPref.get(expected) is not None:
                output += countPref[expected]
                
            if countPref.get(prefix) is not None:
                countPref[prefix]+=1
            else:countPref[prefix]=1
        
        return output
        
        
        
        
        
        '''counter = 0 # TLE
        for i in range(len(A)):
            temp = 0
            for j in range(i,len(A)):
                if A[j] % 2==1:temp +=1
                if temp == B:counter +=1
                if temp > B: # musi byc dokładnie B nieparzystych
                    break
        return counter'''
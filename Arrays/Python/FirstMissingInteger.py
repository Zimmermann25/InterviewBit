class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        
        '''A = list(filter(lambda x : x > 0, A))
        A = [len(A) + 2] + A
        for i, num in enumerate(A):
            num = abs(num)
            if num < len(A):
                A[num] = - abs(A[num])
        for i in range(1, len(A)):
            if A[i] > 0:
                return i
        return len(A)'''
        
        max_ = max(A)
        if max_ <= 0 :
            return 1
        else :
            A=set(A)
            for i in range(1,max_) :
                if i not in A :
                    return i
            return max_ + 1
        
        
        '''if len(A) < 1:return 1
        for i in range(len(A)):
            curVal = A[i]
            
            # umieszczenie jej na wskazanym indeksie
            while 1 <=curVal<=len(A) and A[A[i]-1] != A[i]:
                A[i], A[curVal-1] = A[curVal-1], A[i]
                curVal = A[i]
                
        
        for i in range(len(A)):
            if A[i] != i+1:
                return i+1
        
        return len(A)+1 # jak przypadek 1234...'''
        



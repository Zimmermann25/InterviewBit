class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    #For the purpose of this problem, assume that all the numbers in the collection are unique.
    
    #inny wynik w submit, a inny wynik w custom input, nie działa
    #okej, tym co powoduje problem w takich sytuacjach jest umieszczanie
    #zmiennych globalnych
    
    def permute(self, A):
        A.sort()
        if len(A)==1:return [A]
        output = []
        
        def f(A, start, stop):
            if start==stop:#by długosc podtablicy tablicy się zgadzała
                output.append(A[:])
            else:
                for i in range(start, stop + 1):
                    A[start], A[i] = A[i], A[start]
                    f(A, start + 1, stop)
                    A[start], A[i] = A[i], A[start]  # backtrack
        
        f(A[:], 0, len(A)-1)
        #output.sort()
        
        return output
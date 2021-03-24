class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # chyba nawet bez dodatkowej tablicy output mozna to zrobic
        output = [None] * (len(A))
        for i in range(len(A)):
            j = 0
            while j < i:
                if A[i] == output[j]:
                    output[j] +=1
                    break
                j+=1
            output[i] = A[i]
            
        return output  
        
        #opcjonalne z odpowiedzi, A.index znajduje pierwsze wystąpienie
        #if(A[i] in A and A.index(A[i])<i):
            #A[A.index(A[i])] = A[A.index(A[i])]+1
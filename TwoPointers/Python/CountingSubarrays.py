class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        if len(A) < 1:return 0
        counter = 0
        first = 0
        second = 0
        suma = A[0]
        
        #if suma < B:counter +=1
        while first < len(A) and second < len(A):
            #print("suma: ",suma,"counter: ",counter,"first: ", first, "second: ", second)
            if suma < B:
                second += 1
                counter += max(0, (second - first))
                if second < len(A):
                    suma += A[second]
                
            if suma >=B:
                suma -= A[first]
                first += 1
            
        return counter

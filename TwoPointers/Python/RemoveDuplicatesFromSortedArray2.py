class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):

        if len(A) <=2: return len(A)
        counter = 2 # jako counter, od tego miejsca zaczynam, zawsze co najmniej 2 elementy
        #jesli len(A) >=2
        right = 2
        while right < len(A):
            # sprawdz, czy index i oraz i+2 są różne, jeśli tak, to wartość indeksu right
            # przepisz do indeksu left
            if A[counter-2] != A[right]:
                
                A[counter] = A[right]
                counter +=1
            right +=1
        
        return counter
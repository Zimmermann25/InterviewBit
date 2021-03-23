class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        Acopy = A[::-1]
        # sprawdz, czy juz jest palindromem
        
        left = 0
        right = len(A)-1
        counter = 0
        #print("Acopy: ", Acopy)
        while left <=right:
            if A[left] == A[right]:
                left +=1
                right -=1
            else: # jak są różne, to przesuwaj tylko lewy wskażnik
                if left==0:
                    counter +=1
                    right -=1
                else:
                    counter += left
                    left = 0
            #print("left: ", left, "right: ", right, "counter: ", counter)
        
        return counter
        
        
        
        
            
        
        
        
        

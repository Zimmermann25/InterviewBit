class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        #tutaj liczby trzymane jako A = x + ny
        n = len(A)
        for i in range(n):
            #print(i, A[i])
            A[i] += (A[A[i]]%n)*n #reszta z dzielenia razy n, apotem /n
            #print(A)
            
        for i in range(n):
            A[i] = A[i]//n
        '''temp = A[:]
        
        for i in range(len(A)):
            curVal = A[i]
            nextVal = A[curVal]
            temp[i] = nextVal
            #print("curVal: ", curVal, "nextVal: ", nextVal, "arr: ", A, "temp: ", temp)
        
        A[:] = temp'''
        return
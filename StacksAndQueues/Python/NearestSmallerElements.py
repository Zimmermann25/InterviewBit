class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        G = [-1] * len(A) # -1, bo to ułatwi trochę
        
        curMin = A[0]
        stack = []
        for i in range(len(A)-1):
            #print(stack)
            if stack:
                # dodawaj na stos tylko te elementy, które mogą powodować zmianę
                if A[i] < A[i+1]:
                    
                    '''for k in range(len(stack)):
                        if len(stack) and stack[-k-1] > A[i]:
                            stack.pop()'''
                    stack.append(A[i])
                
                # znajdz w stosie pierwszy element spełniający ten warunek(mniejszy niz A[i])
                for j in range(len(stack)):
                    if stack[-j-1] < A[i]:
                        G[i] = stack[-j-1]
                        break

            else: stack.append(A[i])
            
            #print("stack: ", stack)
        
        # dla ostatniego elementu edge case
        for j in range(len(stack)):
            if stack[-j-1] < A[-1]:
                G[-1] = stack[-j-1]
                break
        
        return G
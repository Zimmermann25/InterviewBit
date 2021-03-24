class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        
        
        stack = []
        for i in range(len(A)):
            
            if A[i] == "(":
                stack.append(A[i])
            #elif A[i] == ")":
                
            elif (A[i]=="+" or A[i]=="-" or A[i]=="/" or A[i]=="*") and len(stack) > 0:
                stack.pop()
                
        
        if len(stack) >0:return 1 #jak cos zostalo, to zwroc 1, redundantt brace
        else:return 0 # jak stack pusty, to zwroc 0
        
        
        

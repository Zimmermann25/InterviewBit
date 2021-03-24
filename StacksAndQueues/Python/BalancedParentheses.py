class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        
        stack = []
        
        for i in range(len(A)):
            
            if A[i] == "(":
                stack.append("(")
            elif A[i] == ")":
                if stack:
                    stack.pop()
                else:
                    return 0 # not balanced
                    
        if stack:return 0
        else:return 1 # balanced
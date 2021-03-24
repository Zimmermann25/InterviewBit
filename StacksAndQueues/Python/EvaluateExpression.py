class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        
        stack = []
        for i in range(len(A)):
            # sprawdzic ascii
            #print(stack)
            
            if A[i] == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a+b)
            elif A[i] == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b-a)
            
            elif A[i] == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a*b)
            elif A[i] == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(int(b/a))
                
            
            else:
                #print("i: ", i)
                stack.append(int(A[i]))
                
               
               
        return stack[0] 
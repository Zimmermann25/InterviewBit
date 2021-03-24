class Solution:
    # @param A : list of integers
    # @return an integer
    # rozwiązanie na podstawie tech dose yt, samemu tylko O(N^2)
    def largestRectangleArea(self, A):
        
        curMax = 0
        stack = []
        LeftSmaller = [None] * len(A)
        RightSmaller = [None] * len(A)
        
        # wartosci mniejsze po lewej stronie po kolei dla kazdego indesku
        for i in range(len(A)):
            if len(stack)==0:
                LeftSmaller[i] = 0
                stack.append(i)
                
            else:
                while len(stack)>0 and  A[i] <= A[stack[-1]]:
                    stack.pop()
                
                if len(stack)==0:
                    LeftSmaller[i] = 0
                else:
                    LeftSmaller[i] = stack[-1] + 1
                
                stack.append(i)
        #print(LeftSmaller)
        stack = [] # usuniecie pozostalosci
        
        
        #wartosci mniejsze po prawej stronie, zaczynam od prawej strony A
        for i in range(len(A)-1, -1, -1):
            if len(stack)==0:
                RightSmaller[i] = i
                stack.append(i)
            else:
                while len(stack)>0 and  A[i] <= A[stack[-1]]:
                    stack.pop()
                
                if len(stack)==0:
                    RightSmaller[i] = len(A)-1
                else:
                    RightSmaller[i] = stack[-1] - 1
                
                stack.append(i)
        #print(RightSmaller)
        
        for i in range(len(A)):
            width = RightSmaller[i] - LeftSmaller[i] + 1
            if width*A[i] > curMax:
                curMax = width*A[i]
        
        
        return curMax
        
        

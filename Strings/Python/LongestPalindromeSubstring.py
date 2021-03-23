class Solution:
    # @param A : string
    # @return a strings
    
    def checkPal(self, A, left, right):
        while left >=0 and right < len(A):
            if A[left] != A[right]:
                break
            
            left -=1
            right +=1
        
        return [left, right]
        
        
    
    def longestPalindrome(self, A):
        if len(A) < 1:return ""
        i = 0
        curMax = 0
        curMaxStr = ""
        firstIndex = 0
        laxtIndex = 0
        while i < len(A):
            #print("i: ", i, "str: ", curMaxStr, "max: ", curMax)
            # dla nieparzystych
            left = i
            right = i
            while left >=0 and right < len(A) and A[left] == A[right]:
                left -=1
                right +=1
                
            # -1, bo po wyjsciu z while left jest zmniejszone, a right ziwększone
            if (right - left - 1) > curMax: 
                curMax = (right - left - 1)
                # ten zapis wynika z tego, ze left jest zmniejszane, a right zwiększane
                #w pętli while przed wyjściem
                curMaxStr = A[left+1:right]
            #print("--i: ", i, "str: ", curMaxStr, "max: ", curMax, 'l:', left, 'r: ', right)
            # dla parzystych
            left = i
            right = i+1
            while left >=0 and right < len(A):
                if A[left] != A[right]:
                    break
                
                left -=1
                right +=1
            
            if (right - left - 1) > curMax:
                curMax = (right - left - 1)
                curMaxStr = A[left+1:right]
            
            #print("----i: ", i, "str: ", curMaxStr, "max: ", curMax)
            i +=1
        
        
        
        return curMaxStr
        
        
        
        

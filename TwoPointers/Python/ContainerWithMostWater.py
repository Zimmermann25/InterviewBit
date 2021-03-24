class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        
        if len(A)<2:
            return 0
        
        i = 0
        curMax = 0
        j = len(A)-1
        lastMin = min(A[i], A[j])
        lastMax = max(A[j], A[i])
        while i < j :
            #kadane dodac
            if min(A[j], A[i]) > lastMin:
                lastMin = min(A[j], A[i])
            base = j - i
            curArea = base * lastMin
            #print("base: ", base, " A[j]:", A[j], "A[i]: ", A[i], "lastMin: ", lastMin)
            if curArea > curMax:
                curMax = curArea
                #lastMin = min(A[j], A[i])
                
               
            #jak mam słupki 3 po lewej i 5 po prawej, to większy słupek(prawy zostaje bez zmian 
            #a lewy słupek musze przesunąć
            if A[i] <= lastMin:
                i+=1
            else:
                j-=1
            #elif A[j] <= lastMin:
                
                
            
        return curMax
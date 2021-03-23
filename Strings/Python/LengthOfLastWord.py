class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        beginningOfTheEnd = 0
        curLength = 0
        A = A.strip()
        for i in range(len(A)):
            if A[i] == " ":
                beginningOfTheEnd = i
                
        
        if beginningOfTheEnd!=0:
            out = len(A)-1 - beginningOfTheEnd
        else:out = len(A)
        
        return out
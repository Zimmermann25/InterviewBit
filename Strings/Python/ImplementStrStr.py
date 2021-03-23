class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        
        for i in range(len(A) - len(B) + 1):
            #print("--")
            found = True
            for j in range(len(B)):
                #print(A[j+i], B[j])
                if B[j] != A[j+i]:
                    found = False
                    break
            
            if found:
                return i
                
        return -1
                
        
        

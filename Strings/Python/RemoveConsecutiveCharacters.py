class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def solve(self, A, B):
        
        if len(A) < 1: return ""
        
        out = ""
        i = 0
        counter = 0
        prevChar = A[0]
        while i < len(A):
            if A[i] == prevChar:
                counter +=1
                
            else: # jak znajde następny znak
                #print("else", out, "cunter: ", counter)
                if counter != B:
                    for j in range(counter):
                        out += prevChar
                        #print(out, "prev: ", prevChar)
                
                prevChar = A[i]
                counter = 1
            
            i+=1
    
        #cornar case dla liter na koncu po wysjciu z while
        if counter != B:
            for i in range(counter):
                out += prevChar
            
        return out
        

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = A.strip()
        arr = []
        i = 0
        while i <len(A):
            lower = i
            upper = i
            if A[i] != " ":
                while upper <= len(A):
                    #print(i, upper)
                    
                    if upper==len(A) or A[upper] == " ":
                        if lower < upper:
                            #print("founded: ", A[lower:upper])
                            arr.append(A[lower:upper].strip())
                            break
                    upper += 1
                
                
            i += (upper - lower)+1
        #print(arr)
        return " ".join(arr[::-1])
        
        
        

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if len(A) < 1:return 0
        
        
        end = 0
        prev = 0
        usedB = 0
        counter = 0 # albo end i prev 
        maxOut = 0
        while prev < len(A) and end < len(A):
            #print("end: ", end, "prev: ", prev, "used: ", usedB, "c: ", counter, "A: ", A[end]) 
            if A[end] ==1:
                end +=1
            elif A[end]==0:
                if usedB < B:
                    usedB +=1
                    end +=1
                else:
                    while prev < len(A) and A[prev] != 0:
                        prev +=1
                    
                    prev +=1 # znalazłem zero, ale właśnie je chce ominąć, wiec +1
                    usedB -=1
                    
            
            counter = end - prev 
            #print("end: ", end, "prev: ", prev, "used: ", usedB, "c: ", counter) 
            
            if counter > maxOut: maxOut = counter

        return maxOut
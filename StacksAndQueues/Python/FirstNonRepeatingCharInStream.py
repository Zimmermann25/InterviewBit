class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        queue = []
        output = ""
        hash = {}
        
        
        #to działa, zrobione jako pierwsze
        for i in range(len(A)):
            if hash.get(A[i]) is not None:
                hash[A[i]] +=1
            else:
                hash[A[i]] = 1
            
            if hash[A[i]] ==1: # piewsze wystąpienie
                queue.append(A[i])
            else:
                for k in range(len(queue)):
                    if queue[k] == A[i]:
                        queue.pop(k)
                        break
            
            if len(queue) >=1:output += queue[0]
            else:output += "#"

        return output
            
        
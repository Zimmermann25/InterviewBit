class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        
        Abigger = True if len(A) > len(B) else False
        biggerLength = len(A) if len(A) >= len(B) else len(B)
        counterA = 0
        counterB = 0
        lengthSum = len(A) + len(B)
        '''while counterA + counterB <= lengthSum:
            #print(counterA, counterB, A, len(A))
            if counterA < len(A):
                Aval = A[counterA]
            else:
                A.extend(B[counterB:])
                #print("firest else")
                break
            
            if counterB < len(B):   
                Bval = B[counterB]
            else:
                #print("secondElse")
                break
            
            if Aval < Bval:
                counterA+=1
                pass
            elif Aval >= Bval:
                A.insert(counterA, Bval)
                counterB += 1
                counterA += 1# zwiekszenie ze wzgledu na insert above'''
        
        # with aux array
        C = [None] * (len(A) + len(B))
        i = 0
        while counterA + counterB <= (len(A) + len(B)):
            if counterA < len(A):
                Aval = A[counterA]
            else:
                for i in range(counterB, len(B)):
                    C[counterA+i] = B[i]
                #print("firest else")
                break
            
            if counterB < len(B):   
                Bval = B[counterB]
            else:
                for i in range(counterA, len(A)):
                    C[i+counterB] = A[i]
                #print("secondElse")
                break
            
            if Aval < Bval:
                C[counterA + counterB] = Aval
                counterA+=1
                pass
            elif Aval >= Bval:
                C[counterA + counterB] = Bval
                counterB += 1
                
            #print(C)
        
        
        A[:] = C[:]
            
            
        

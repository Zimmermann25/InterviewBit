class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        '''while(i<j){
            if(count>1) return 0;
            if(A[i]==A[j]) i++,j--;
            else if(A[i]!=A[j] && A[i+1]==A[j]) i++,count++;
            else if(A[i]!=A[j] && A[i]==A[j-1]) j--,count++;
            else return 0;
        }
        
        if(i==j && count>1) return 0;
        return 1;'''
        if len(A) < 1:return 0
        # jak wchodzi parzysta dlugosc, usuwam 1 znak, bedzie nieparzysta
        
        left = 0
        right = len(A)-1
        used = 0
        while left < right:
            
            if A[left] == A[right]:
                right -=1
                left +=1
            elif A[left+1] == A[right]:
                used +=1
                left +=1
            elif A[left] == A[right-1]:
                right -=1
                used +=1
            else: # jeśli trzeba by bylo minimum 2 zmienić
                return 0
            if used > 1: return 0
                
        return 1
        


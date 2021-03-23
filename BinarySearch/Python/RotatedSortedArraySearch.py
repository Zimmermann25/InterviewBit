class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        
        #peak finding algorithm, będzie tylko jeden peak(pivot), zerowy lub ostatni 
        #element oznacza brak pivota,  pivot % len(A)==0
        low = 0
        high = len(A)-1
        halfIndex = 0
        while low <=high:
            mid = (low + high)//2
            if mid<0 or mid >= len(A)-1:
                break
            
            if A[mid - 1] <= A[mid] and A[mid] >= A[mid + 1]:
                halfIndex = mid
                break
            elif A[mid] <= A[0]:  # peak po lewej stronie mida
                high = mid - 1
            else:
                low = mid + 1

        
        #print("halfIndex: ", halfIndex)
        low = 0
        high = halfIndex
        
        while low <= high:
            mid = (low + high) // 2
            #if mid <0:break
            #print("mid: ", mid, "low: ", low, "high: ", high, "A[mid]: ", A[mid])
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid - 1

        # jesli nie znaleziono w lewej części, to szukaj w prawej(też rosnąca)
        low = halfIndex+1 # zwróciło uwagę na to +1
        high = len(A) - 1

        #print("brefore second")
        while low <= high:
            mid = (low + high) // 2
            #print("mid: ", mid, "low: ", low, "high: ", high, "A[mid]: ", A[mid])
            #if mid < 0: break
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid - 1

        return -1
        
        
        
        
        
        
        
        
        
        
        

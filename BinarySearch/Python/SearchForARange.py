class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        
        if len(A) < 1:return []
        # najierw first occ
        low = 0
        high = len(A)-1
        out = []
        found = False
        while low <= high:
            mid = (low + high)//2
            
            if A[mid]==B:
                found = True
                high = mid -1
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid-1
        
        if found:
            out.append(low)
            found = False # do drugiel petli
        else:
            return [-1, -1]
        
        high = len(A)-1
        #print("low: ", low, "high: ", high)
        while low <= high:
            mid = (low + high)//2
            
            if A[mid]==B:
                found = True
                low = mid+1 # jak znajdziesz, to sprobuj przejsć na następną pozycję
                #ale jeśli to była ostatnia wartość, to +1 będzie już nastepną liczbą
                # dlatego jeśli jest ostatnie wystąpienie to return high
                # a jak pierwsze to return low
            elif A[mid] < B:
                low = mid + 1
            else:
                high = mid-1
                
        #print("low: ", low, "high: ", high)
        out.append(high)
        return out
        
        
        
        
        
        
        
        

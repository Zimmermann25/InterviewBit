class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        if len(A) < 3:return []
        
        A.sort()
        out = []
        
        # indeksy z tablicy
        first = 0
        while first < len(A)-2: # outer loop, element first stały indeks
            if A[first] >0: # bo posortowane
                break
            second = first+1
            third = len(A)-1
            while second < third:
                suma = A[first] + A[second] + A[third]
                if suma == 0:
                    arr = (A[first], A[second], A[third])
                    #print(arr in A)
                    #if arr not in out:
                    out.append(arr)
                    second +=1
                elif suma < 0:
                    second +=1
                elif suma > 0:
                    #if A[second] + A[third] > -A[first]:
                        
                    third -= 1
            first += 1
        s = set(out)
        #print(s)
                
        return sorted(s)
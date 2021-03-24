class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        
        temp = A
        arr = []
        while temp > 0:
            arr.append(temp % 10)
            temp //=10
        
        arr = arr[::-1]
        #print(arr)
        #countDigits
        digits = len(str(A))
        #print("digits: ", digits)
        hash = set()
        i = 0
        j= 0
        while i < digits:
            curProd = 1 # element nuetralny mnozenia
            j = i
            while j < digits:
                curProd *= arr[j]
                if curProd in hash:
                    return 0
                else:
                    hash.add(curProd)
                
                j+=1
            i +=1
        
        return 1
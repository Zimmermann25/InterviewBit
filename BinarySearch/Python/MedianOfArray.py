class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    
    # znajdz ile jest mniejszych wartosci niz val
    def firstOccIndex(self,arr, val):
        left = 0
        right = len(arr) - 1
        found = False
        mid = (left + right) // 2
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == val:
                found = True
                right = mid -1
            elif arr[mid] < val:
                left = mid + 1
            else:
                right = mid - 1
    
        return (left, found) # zwraca ile wartosci w tablicy jest MNIEJSZYCH niz val
    
    
    def lastOccIndex(self,arr, val):
        left = 0
        right = len(arr) - 1
        found = False
        mid = (left + right) // 2
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == val:
                found = True
                left = mid +1
            elif arr[mid] < val:
                left = mid + 1
            else:
                right = mid - 1
        return (len(arr)- right - 1, found)# zwraca ile wartosci w tablicy jest WIEKSZYCH niz val
    
    
    def findMedianSortedArrays(self,A, B):
        if len(A) <1:
            if len(B) % 2==0:
                return (B[len(B)//2 - 1] + B[len(B)//2] ) / 2.0
            else:
                return B[len(B)//2]
        
        if len(B) <1:
            if len(A) % 2==0:
                return (A[len(A)//2 - 1] + A[len(A)//2] ) / 2.0
            else:
                return A[len(A)//2]
                
                
        
        
        evenLen = True if (len(A) + len(B)) % 2 == 0 else False
        minBoth = A[0] if A[0] <= B[0] else B[0]
        maxBoth = A[-1] if A[-1] >= B[-1] else B[-1]
        if evenLen:
            smallerFromLeft = ((len(A) + len(B)) // 2) - 1
            biggerFromRight = ((len(A) + len(B)) // 2)
            #smallerFromLeft = biggerFromRight = (len(A) + len(B)) // 2
        else:
            smallerFromLeft = biggerFromRight = (len(A) + len(B)) // 2
    
        leftVal = 0
        rightVal = 0
        for i in range(2):
            leftDiff = 0
            rightDiff = 0
            mid = 0
            minBoth = A[0] if A[0] <= B[0] else B[0]
            maxBoth = A[-1] if A[-1] >= B[-1] else B[-1]
            while minBoth <= maxBoth:
                mid = (minBoth + maxBoth)//2
                Afirst = self.firstOccIndex(A, mid) # ile elementow mniejszych niz mid w A
                Bfirst = self.firstOccIndex(B, mid)
                Alast = self.lastOccIndex(A, mid)
                Blast = self.lastOccIndex(B, mid)
    
                # latwiejszy, dla nieparzystych
                #print("Afirst: ", Afirst[0], "Bfirst: ", Bfirst[0], "Alast: ", Alast[0], "Blast: ", Blast[0], "mid: ", mid, "smaller: ", smallerFromLeft,
                      #"bigger: ", biggerFromRight)
                if not evenLen:
                    if Afirst[0] + Bfirst[0] <= smallerFromLeft and Alast[0] + Blast[0] <=biggerFromRight: # oba warunki mediany spełnione
                        #print("return")
                        return mid
                    elif Afirst[0] + Bfirst[0] <= smallerFromLeft:
                        minBoth  = mid+1
                    else:
                        maxBoth = mid-1
                elif evenLen:
                    # jeszcze przypadek na parzystosc, w tym ifie znalazlem pierwsza z dwóch liczb ( leftVal)
                    # szukam najmniejszej róznicy miedzy wystąpieniami z lewej i oczekiwanymi, oraz to damo dla prawej
                    if i==0: # binary search dla lewej połowy
                        if Afirst[0] + Bfirst[0] <= smallerFromLeft :
                            if Afirst[0] + Bfirst[0] >= leftDiff: #maksymalna ilość mniejszych od smallerFromLeft
                                leftDiff = Afirst[0] + Bfirst[0]
                                if Afirst[1] or Bfirst[1]:
                                    leftVal = mid
    
                            # jeszcze zwiększenie left
                            minBoth = mid+1
                        else:
                            maxBoth = mid -1
    
                    elif i==1: # binary search dla większego elementu
                        if Alast[0] + Blast[0] < biggerFromRight:
                            if Alast[0] + Blast[0] >= rightDiff:
                                rightDiff = Alast[0] + Blast[0]
                                #print(Alast[1], " ", Blast[1], "mid: ", mid, "rightVal: ", rightVal)
                                if Alast[1] or Blast[1]:
                                    rightVal = mid
                            maxBoth  = mid -1
                        else:
                            minBoth = mid +1
        
    
        if evenLen:
            #print("left: ", leftVal, "right: ", rightVal)
            return (leftVal + rightVal)/2.0
        return mid
        
        
        
        







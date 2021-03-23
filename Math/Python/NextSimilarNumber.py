class Solution:
    # @param A : string
    # @return a strings
    #THAT WAS A HELL OF A RIDE XDDDD, 30 min -> 2.5H
    def solve(self, A):
        # 2 special case dla sorted i unsorted jeszcze
        if len(A) < 2: return -1
        arr = [A[i] for i in range(len(A))]
        
        # jeśli posortowana rosnąco
        isSorted = True
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                isSorted = False
                break
        if isSorted: 
            #print(arr[-1], " ", arr[-2])
            arr[-1], arr[-2] = arr[-2], arr[-1]
            return "".join(arr)
        
        isSorted = True # jeśli posortowana malejąco
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                isSorted = False
                break
        if isSorted:return -1
            
        lastDigit = arr[-1]
        upToIndex = 0
        # idąc od końca znajdź pierwszą liczbę, która jest mniejsza od poprzedniej
        i = len(arr)-2
        while i >=0:
            #print("A[i]: ", A[i], "last: ", lastDigit, "upTo: ", upToIndex, "i: ", i)
            if arr[i] < arr[i+1]:
                upToIndex = i
                break
            i-=1
        i = upToIndex+1 #od indeksu po znalezionej znajdź większą liczbę od niej
        # ale możliwie najmniejszą
        foundIndex = 0
        upDigit = arr[upToIndex]
        maxDigit = '9'
        while i < len(A):
            #print("i: ", i,  "upTo: ",upToIndex, "arr: ", arr, "upDigit: ", upDigit)
            if arr[i] > upDigit and arr[i] <= maxDigit :
                maxDigit = arr[i]
                foundIndex = i
                #print("found: ", arr[i], "i: ", i)
            i+=1
        
        #print("upTo: ", upToIndex, "found: ", foundIndex, "max: ", maxDigit) 
        if foundIndex:
            arr[upToIndex], arr[foundIndex] = arr[foundIndex], arr[upToIndex] 
        

        #print("part of array: ", arr[upToIndex+1:])
        # posortuj pozostałe elementy( mozna rownież zrobić po prostu ich reverse)
        temp = sorted(arr[upToIndex+1:])
        arr[upToIndex+1:] = temp

        
            
            #print("i: ", i, "k: ", k, "upTo: ",upToIndex, "arr: ", arr)
           
            
        #print(arr)
        return "".join(arr)
        
        '''swapped = True
        upToIndex = len(arr)-2
        while swapped:
            lastDigit = arr[-1]
            i = upToIndex
            swapped = False
            print("firstWhile", i)
            while i >=0:
                print("A[i]: ", A[i], "last: ", lastDigit, "upTo: ", upToIndex)
                if arr[i] < lastDigit:
                    #swap
                    arr[i], arr[-1] = arr[-1], arr[i]
                    swapped = True
                    upToIndex = i
                i-=1
        
        return "".join(arr)'''
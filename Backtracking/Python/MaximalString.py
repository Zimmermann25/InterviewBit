class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    #backtrack naciagany na siłe, w cpp dla ponizszych danych program sie wywala
    # a tutaj iteracyjnie wszystko git, ale nie zalicza rozwiązania
    #10343456789765432457689065543876
    #10
    # w c++ backtracking z komentarza jest uznawany, choć dla długości A ~kilkanaści juz się
    #wysypuje xdddddddd, tu działa poprawnie i nie jest uznawany :(
    def solve(self, A, B):
        arr = list(A)
        
        counter = 0
        i = 0
        while i < len(arr):# tak jak w selection sort, ale tutaj maks B swapów
            maxIndex = i
            k = i+1
            #print("A[maxIndex]: ", arr[i], "arr: ", arr, "i: ", i)
            while k < len(arr):
                if arr[k] > arr[maxIndex]: # co z >=??
                    maxIndex = k
                if arr[k]==9:break
                k+=1
            
            if maxIndex!=i:#sprawdz, czy wykonac swap
                arr[i], arr[maxIndex] = arr[maxIndex], arr[i]
                counter +=1
            if counter ==B:break
            i +=1
        return "".join(arr)
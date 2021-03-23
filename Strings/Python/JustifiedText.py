class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    # wazne założenie, długość pojedynczego wyrazu <=16
    def fullJustify(self, A, B):
        if len(A) < 1:return []
        
        i = 0
        prev = 0
        tempSum = 0
        outArr = []
        tempStr = ""
        howMany = 0  # ile napisów zmieści się w danej linii
        while i < len(A):
            if A[i] !="":
                tempSum += len(A[i])
                howMany += 1
                #print("i:", i, "prev: ", prev, "tempSum: ", tempSum, "tempStr: ", tempStr, "A[i]", A[i])
                if tempSum == B:
                    while prev < i: # bo ostatni w linii bez spacji
                        tempStr += (A[prev] + " ")
                        prev+=1
                    tempStr += A[i]
                    outArr.append(tempStr)
                    prev = i+1 # +1, bo aktualny napis się nie będzie wliczał
                    tempStr = ""
                    tempSum = 0
                    howMany = 0 # tutaj równiez 0 zamiast 1, bo akutalny się nie wliczy
    
                elif tempSum < B:
                    tempSum += 1  # spacja
    
                elif tempSum > B:  # napisy z zakresu indeksów prev -> i
                    last = i - 1
                    tempSum -= (len(A[i]) + 1)  # +1 bo jeszcze odejmuje dodaną spację
                    # tutaj sprawdzić edge cases dla -2
                    tempSum -= (howMany-2) # ile spacji wcześniej zostao dodanych
                    howMany -= 2  # odjęcie nadmiarowego wyrazu, a do ostatniego nie dodaje spacji, czyli -2

                    if howMany > 0:
                        full, rem = divmod(B - tempSum, howMany)
                    else: 
                        # jak howMany=0, to while się nie wykona, dodaj spacje na koncu napisu
                        full = B - tempSum
                        rem = 0
    
                    while prev < i - 1:
                        tempStr += A[prev]
                        # oblicz sumę + spację, (ostatnie bez spacji)
                        if rem > 0:# dodawaj pozostałe spacje az się wyczerpią
                            tempStr += (" " * (full + 1))
                            tempSum += (full + 1)
                            rem -= 1
                        else: # jak sie wyczerpią, to tyko stałą ilość
                            tempStr += (" " * full) # 
                            tempSum += full
                        # print("tempStr: ", tempStr)
                        prev += 1
    
                    d = B - tempSum
                    tempStr += (A[i - 1] + (" " * d)) # jeśli tylko jeden wyraz, to totaj doda zera na koncu
                    #tempStr += A[i-1] # ostatnic wyraz, do którego nic nie dodaje
                    outArr.append(tempStr)
                    prev = i
                    howMany = 1
                    tempStr = ""  # zeby nie stracić informacji o elemencie, który przekroczy
                    tempSum = len(A[i])+1 # bo spacja by default z nim
                    #print("howMany: ", howMany, "tempSum: ", tempSum, "last: ", last, outArr)
            i += 1

        # jeszcze osobno dla ostatniego wiersza i napisu, ich suma <=16
        #print('tempSum: ', tempSum)
        if tempSum>0:
            while prev < i - 1: # ostatni wiersz, wyrazy przed ostatnim
                tempStr += (A[prev] + " ")
                # oblicz sumę + spację, (ostatnie bez spacji)
                prev +=1

            tempStr += A[i-1] # ostatni napis w tablicy
            diff = B - len(tempStr)
            outArr.append((tempStr + (" " * diff)))

        return outArr
            
            
            
        
        
        
        
        

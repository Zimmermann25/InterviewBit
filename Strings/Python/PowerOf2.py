class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        
        if len(A)==1 and int(A[0]) ==1:return 0
        if int(A[-1]) % 2 != 0 and int(A[0]) != 1: return 0  # jesli nieparzysta na koncu, to False
        if int(A[0]) < 1: return 0
        
            
        j = 0
        n = len(A)
        A2 = list(A)
        while A2[len(A2)-1] != '1' or j != len(A2)-1:
            j = 0
            num = 0
            if (ord(A2[n-1]) - 48) % 2 == 1:return 0
            while A2[j]=='0':
                j += 1
  
            for i in range(j, n):
                num = num * 10 + (ord(A2[i]) - 48)
                #print("num: ", num, "ord: ", ord(A2[i]), "e: ", (num//2) + 48)
                #print(chr((num//2) + 48))
                A2[i] =  chr((num//2) + 48)
                num %=2
            
        
        return 1
        
        '''if int(A[-1]) % 2 != 0 and int(A[0]) != 1: return 0  # jesli nieparzysta na koncu, to False
        if int(A[0]) < 1: return 0
    
        temp = [0] * len(A)  # backwards
        temp[-1] = 1
        i = 0
    
        # TLE
        outerLoop = True
        firstNonZero = len(A) - 1
        counter =100
        while outerLoop:
            j = firstNonZero
            if j < 0:break
            carry = 0
            while j < len(temp):  # przejscie po wartosciach, przypadek z zerem do break
    
                if temp[j] * 2 >= 10:
                    if firstNonZero >=1:
                        firstNonZero -= 1
                    carry = (temp[j] * 2) // 10
                    temp[j] = (temp[j] * 2) - 10
                    temp[j - 1] += carry
                else:
                    temp[j] *= 2
                j += 1
            #print("temp: ", temp, "j: ", j, "first: ", firstNonZero)
            if temp[0] > 0:
                curStr = "".join(map(str, temp))
                if curStr == A:
                    return 1
    
            if temp[0] * 2 >= 10:  # tu juz tablica musialaby byc dluzsza niz napis
                outerLoop = False
                break  # przerwanie petli
            i += 1
        return 0'''
                
        
        
        
        
        
        
        

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    # nie mam pjęcia, czemu jest partially correct, w cpp niemalże identyczny
    #kod uznaje, a tutaj nie
    # mozna to było uproscic, bo ja działałem na unikalności licznika
    # a w rozwiązaniach działania na unikalności reszty z dzielenia
    def fractionToDecimal(self, A, B):
        if A ==0:return "0"
        i = 0
        if (A < 0 and B < 0) or (A > 0 and B > 0):
            fixedBeginning = ""
        else:fixedBeginning = "-"
        
        A = abs(A)
        B = abs(B)
        fullPart = A // B
        rem = A % B
        fixedBeginning += str(fullPart)
        A -= B*fullPart # bo ponizej interesuje mnie tylko część ułamkowa
        
        afterComa = ""
        usedValues = dict()  # dict, bo jeszcze indeksy początkowe potrzebne
        while (A*10)<B:
            afterComa += "0"
            #print("A: ", A*10)
            usedValues[A*10] = i # tutaj nie mogą się powtorzeyc bo zwiekszam razy 10
            A *=10
            i+=1
        startIndex = 0
        while True:
            A *= 10
            if usedValues.get(A) is not None:
                startIndex = usedValues[A]
                break
            else:
                usedValues[A] = i  # indeks początkowy
            #print("out: ", out, "i: ", i, "A: ", A, usedValues)
            full = A // B
            rem = A % B
            A -= (B * full)
            afterComa += str(full)
            if rem == 0:
                i+=1
                return fixedBeginning+ "." + afterComa[:i]
                break
            #print("out: ", out, "A: ", A, "full: ", full)
            i += 1
    
        #print("start: ", startIndex, "stop: ", i, "afterComa: ", afterComa)
        periodStr = "(" + afterComa[startIndex: i] + ")"
        finalAns = fixedBeginning + afterComa[:startIndex] + periodStr
        #print("periodStr: ", periodStr)
        return finalAns
        
        
        
        

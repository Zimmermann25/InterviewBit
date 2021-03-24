class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        # wcześniej było zrobione bez overlapping, to było błędem
        lengthL = len(B[0])
        hash = {}  # liczenie podanych wyrazów w B przy wywolaniu
        tempDict = {}  # do zliczania wystąpień wyrazów w ciągu A
        for i in range(len(B)):
            if hash.get(B[i]) is None:
                hash[B[i]] = 1
                tempDict[B[i]] = 0
            else:
                hash[B[i]] += 1
    
        # co z overlappping???
        output = []
        if len(B)==1:#wtedy string matching only
            for i in range(len(A) - lengthL +1):
                if A[i:i+lengthL] == B[0]:
                    output.append(i)
            return output
        
        i = 0
        j = lengthL
        while i + lengthL <= len(A) :
            leftWord = A[i:lengthL + i]  # zawsze słowo po lewej
            if (i + lengthL*len(B)) > len(A):
                return output
            if leftWord not in hash:i+=1
    
            else: # jak znajdzie lewe slowo, to szukaj pozostałych
                j = i + lengthL
                if j < len(A):tempDict[leftWord] +=1
                while j + lengthL <= len(A):
                    rightWord = A[j:lengthL +j]
                    #print("leftWord: ", leftWord, "right: ", rightWord, "i: ", i, "j: ", j, "dict: ", tempDict)
                    if rightWord in tempDict:
                        tempDict[rightWord] +=1
                        if tempDict[rightWord] > hash[rightWord]: # jak za duzo tego samego wyrazu w tempDict, bez rolling over
                            #print("first if")
                            #tempDict[leftWord] -=1
                            #i += lengthL - 1 # -1, bo zaraz będzie i+=1
                            for key in tempDict.keys():
                                tempDict[key] = 0
                            break
                        elif tempDict == hash:
                            #print("elif")
                            output.append(i)
                            tempDict[leftWord] -= 1
                            i -= 1  # -1, bo zaraz będzie i+=1
                            break
                        else: # jak można kontynuuować
                            #tempDict[rightWord] +=1
                            j+= lengthL - 1
    
                    else: # jak prawego słowa nie ma w slowniku, to przesun lewe słowo do tego miejsca
                        #i = j # zaraz będzie i +=1
                        for key in tempDict.keys():
                            tempDict[key] = 0
                        break
                    j+=1
                i+=1
        # edge case, kiedy na ostatnim indeksei jest slowo dopełniające sekwencje??
        #print(tempDict)
        # print("dict: ", hash)
        return output
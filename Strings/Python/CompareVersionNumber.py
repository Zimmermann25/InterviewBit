class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        
        if len(A)==len(B)==0:return 0
        
        Ai = 1
        Bi = 1
        # tutaj celowo dodane zero jako zerowy indeks, potem w while będzie łatwiej
        Adots = [-1]
        for j in range(len(A)):
            if A[j]=='.':
                Adots.append(j)
        Adots.append(len(A))
        
        Bdots = [-1]
        for j in range(len(B)):
            if B[j]=='.':
                Bdots.append(j)
        Bdots.append(len(B))

        biggerLen = len(Adots) if len(Adots) > len(Bdots) else len(Bdots)
        #print("Adots: ", Adots)
        #print("Bdots: ", Bdots)
        #print("bigger: ", biggerLen)
        i = 0
        while i < biggerLen: # worst case, jeśli cały czas będą takie same
            # znajdz ciąg do pierwszej kropki w napisie A
            Atemp = 0
            Btemp = 0
            if Ai < len(Adots) :
                Abase = 1
                curIndex = Adots[Ai]
                while curIndex-1 > Adots[Ai-1]:
                    #print("Atemp: ", Atemp, "curIndex-1: ", curIndex-1, A[curIndex-1])
                    Atemp += Abase * int(A[curIndex-1])
                    Abase *=10
                    curIndex -=1
                Ai += 1 # by po znalezieniu kropki przejść dalej
                
            if Bi < len(Bdots) :
                Bbase = 1
                curIndex = Bdots[Bi]
                while curIndex-1 > Bdots[Bi-1]:
                    Btemp += Bbase * int(B[curIndex-1])
                    Bbase *=10
                    curIndex -=1
                Bi += 1 # by po znalezieniu kropki przejść dalej
            
            #print("Atemp: ", Atemp, "Btemp: ", Btemp)
            i+=1
            if Atemp > Btemp:
                return 1
            elif Atemp < Btemp:
                return -1
            
        
        return 0 # jesli dotad doszło, to wersje równe
        
        
        

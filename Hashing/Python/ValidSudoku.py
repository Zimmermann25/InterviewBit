class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        # zakladam, ze dlugosc wszystkich podtablic to 9
        #mozna tez było użyć zwykłych tablic 9 elementowych
        #for i in A:
            #print(i)
        
        #walidacja horizontal
        for i in range(9): # numer wiersza
            horizontalSet= set()
            for k in range(9):
                if A[i][k] != ".":
                    if A[i][k] in horizontalSet:
                        #print("horizontalErr")
                        return 0
                    else:horizontalSet.add(A[i][k])
                    
        #walidacja w kolumnach
        for i in range(9): # numer kolumny
            verticalSet = set()
            for k in range(9): # numer wiersza
                if A[k][i] !=".":
                    if A[k][i] in verticalSet:
                        #print("verticalErr")
                        return 0
                    else:verticalSet.add(A[k][i])
        
        # square
        for i in range(9): # ilosc kwadratow
            squareSet = set()
            Row = (i//3) * 3
            
            for j in range(3): # zwiększanie w kolumnie
                Col = (i % 3 ) * 3 + j
                for k in range(3): # zwiekszanie w wierszu ( +k)
                    Row = ((i//3) * 3) + k
                    
                    if A[Row][Col] != ".":
                        if A[Row][Col] in squareSet:
                            #print("squareErr")
                            return 0
                        else:squareSet.add(A[Row][Col])
                            
        
        
        return 1 # valid
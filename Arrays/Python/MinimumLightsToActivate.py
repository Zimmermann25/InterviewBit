class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    
    #realizacja po wykorzystaniu wskazówki
    '''polega na tym, że skaczę po pozycjach, zaczynam od początkowej i szukam maksymalnie po
    prawej żarówki, która obejmie ten obszar. Po znalezieniu przesuwam się do 
    miejsca znalezienia + B, to następna będzie nieoświetlona jeszcze pozycja
    Jeśli nie uda mi się znaleźć nic maksymalnie po prawej, to szukam pierwszego po lewej
    (cofam się max B POZYCJI) jak nic po lewej nie znajde to koniec i nie da się oświetlić
    jak znajde, to od pierwszej znalezionej pozycji przesuwam się o B pozycji w prawo do
    kolejnego nieoświetlonego miejsca i powtarzam aż do końca
    Nie ma potrzeby stosowania backtrackingu
    '''
    
    def solve(self, A, B):
        
        output = 0
        i = 0 # aktualnie sprawdzana, nieoświetlona pozycja
        j = 0
        while i < len(A):
            maxPosition = i
            output +=1
            found = False
            for k in range(B): # musze zacząć od zera, sprawdzam, czy pozycja ma żarówke
                if i+k <len(A) and A[i+k] ==1:
                    maxPosition = i+k
                    found = True
                    
            if found: # jak znajdzie skrajną dostępną po prawej
                i = maxPosition + B # teraz sprawdzanie o B pozycji w prawo od zapalonej
        
            else: # nie znalazłem po prawej, teraz sprawdzam B pozycji w lewo
                #jak nic nie znajde, to wtedy mogę zwrócić -1
                leftFound = False
                for k in range(B):
                    if i-k <0:return -1
                    if A[i-k]==1:
                        i = i-k + B
                        leftFound = True
                        break
                if leftFound==False:return -1 # ciemna strefa, nie da się jej oswietlić
        
        return output
class Solution:
    # @param A : list of integers
    # @return an integer
    # stack, ale tez podobne do sliding window
    def maxSpecialProduct(self, A):
        if len(A) < 3:return 0
        output = 0
        #11 6 5 4 9 9 6 5 4 5 9 9 -> 48
        stack = []
        # pierwszy dolny peak poszukiwany jest, 1,4,3,4 
        # dla równych wartości bierz pietwsze wystąpienie
        # dodawaj na stos kolejne elementy A[i], które są > niz wartość na górze stosu
        #tym sposobem śledzona jest pierwsza z lewej wartość > A[i] (tresc zadania)
        # jak coś na stosie mniejsze niz A[i], to usuwaj tak długo, aż 
        #znajdziesz coś wiekszego, obliczając jednocześnie iloczyn indeksów
        # bo to oznacza, ze warunek z treści zadania jest spełniony dla wartości na stosie(top)
        #(dlatego najpierw pop, by dostać się do pierwszej wartosci po lewej od middleElement)
        
        for i in range(len(A)):
            #print("stack Before: ", stack, "curValue: ", A[i])
            # jak stos pusty, to nie sprawdzaj, po prostu dodaj
            while stack and A[i] >= A[stack[-1]]:
                stack.pop()
                if stack:
                    if i * stack[-1] > output:
                        output = i * stack[-1]

            stack.append(i)
            #print("stackAfter: ", stack, "output: ", output)
        
        # wydaje mi się, że to jest bardzo zbliżone do zadania 1 z nokiathonu
        #również szukam doliny, ale tu potrzebuje pierwszego wystąpienia
        #edit, może jednak nie koniecznie da się to zrobić w czasie O(N)
        # w czasie O(N^2) mozna zrobić na zasadzie ekspansji w lewo i prawo
        
        
        return output % (10**9 + 7)
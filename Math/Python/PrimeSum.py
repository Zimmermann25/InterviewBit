import math
class Solution:
    # @param A : integer
    # @return a list of integers
    # tutaj memory limit polega na tym, ze najpierw generuje wiele liczb pierwszych
    # z których używam tylko dwóch, lepiej generować i sprawdzać adhoc
    def primesum(self, n):
        is_prime = [True for i in range(n+1)] 
        is_prime[0], is_prime[1] = False, False

        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * 2, n + 1, i): # tutaj eliminacja(sito)
                    is_prime[j] = False

        for i in range(2, n): # schodzenie z dwóch stron 
            if is_prime[i] and is_prime[n - i]:
                return [i, n - i]

        return []
    '''def primesum(self, A):
        is_prime = [True for i in range(A+1)]
        curNum = 3
        is_prime[0] = is_prime[1] = False
        for i in range(2, math.ceil(math.sqrt(A))+1):
            curNum = i*2 #*2, bo dopiero kolejne wystąpienie jest niepierwsze napewno
            while curNum <= A:
                is_prime[curNum] = False # 0 oznacza, że liczba nie jest pierwsza
                curNum += i
        
        # dopasowanie sumy
        for i in range(2, A):
            if is_prime[i] and is_prime[A - i]:
                return [i, A - i]
        

        
        
        return [first, last]'''
        


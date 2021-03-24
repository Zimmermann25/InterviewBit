class Solution:
    # @param A : list of integers
    # @return an integer
    # na indeksach nie działało dobrze, musiałem użyć wartosci
    # pierwsze rozwiaznanie ma TLE
    # drugie niesamodzielne, tylko ze wskzówką
    def solve(self, A):
        '''rootArr = [0]
        left = - 2**32
        right = 2**32
        def validate(left, right):
            if rootArr[0] >= len(A): return 1 # wszystko ok
            if not left<A[rootArr[0]] <=right:return 0
            
            end = A[rootArr[0]]
            rootArr[0] +=1
            validate(left, end) # w lewo
            return validate(end, right)# w prawo, ten return jest tutaj wymagany, bez niego nie działa
        
        if validate(left, right):return 1
        else:return 0'''
        
        
        # teraz z użyciem stosu
        stack = []
        root = -2**32
        #root oznacza aktualną najmniejszą wartość, która nie może zostać przekroczona 
        # w kolejnym sprawdzanym poddrzewie
        # najlepier rozpatrzyć przykład np. 7   4 2 1 3 6 5 7
        #jak coś wchodzi w prawą gałąź, to wtedy root staje się maksymalną dozwolona
        #wartością dla tego poddrzewa, jak wejdzie coś mniejszego, to nie jest 
        #wtedy prawidłowe BST
        for i in range(len(A)):
            #print("stack: ", stack, "root: ", root, "Ai: ",A[i])
            if A[i] < root:return 0
            while stack  and A[i] > stack[-1]:
                root = stack.pop()
            stack.append(A[i]) # dołączaj mniejsze elementy niż na szczycie stosu
            #print("AFTER STACK: ", stack, "root: ", root)
    
        return 1
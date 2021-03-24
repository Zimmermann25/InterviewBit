class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    # chyba tutaj używanie innych funkcji w klasie nie działa
    # i wszystko trzeba robić w jednej funkcji
    '''
    Zimmermann ty kretynie -> w pętli for dałem return self.traverse, czyli w pętli for był
    tylko jeden zwrot funkcji zamiast wielu...
    Po usunieciu return działa poprawnie w skróconej na dole wersji
    '''
    #EDIT: to mojego  autorstwa już działa XDD
    def subsets(self, A):
        A.sort()
        output = []
        # do traverse wchodzi posortowane A
        def traverse( AA, curIndex, curArr):
            output.append(curArr[:])
            for i in range(curIndex, len(AA)):
                # print("start: ", start, "i: ", i, "tempArr: ", tempArr)
                curArr.append(AA[i])
                # print("tempArr: ", tempArr, "i: ", i, "curIndex: ", curIndex)
                traverse(AA, i + 1, curArr)
                curArr.pop()
        traverse(A, 0, [])
        return output
    
    
        
        
    # to działa, ale moje nie działało xddddddddddddddddddd    
    '''def subsets(self, A):
        res=[]
        A.sort()
        
        def f(A, subset, index):
            res.append(subset[:])
            for i in range (index, len(A)):
                subset.append(A[i])
                f(A, subset, i+1)
                subset.pop(-1)
            return
        
        f(A, [], 0)
        return res'''
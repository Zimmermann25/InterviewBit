class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    
    # moje:
    '''#nie podoba mi się to rozwiązanie, ale działa
        if curArr not in output:
            output.append(curArr)
        for i in range(curIndex, len(A)):
            tempArr = curArr[:]
            tempArr.append(A[i])
            #print("i: ", i, "curIndex: ", curIndex, "tempArr: ", tempArr)
            f(A, i+1, tempArr)'''
    
    def subsetsWithDup(self, A):
        
        A.sort()
        output = []
        def f(A, curIndex, curArr):
 
            i = curIndex
            output.append(curArr[:])
            while i < len(A):
                curArr.append(A[i])
                f(A, i+1, curArr)
                #print("i: ", i, "curIndex: ", curIndex, "tempArr: ", tempArr)
                #pomin powtarzające isę
                while i < len(A)-1 and A[i] ==A[i+1]:
                    i+=1
                #if(tempArr)
                curArr.pop() # usun poprzedni element
                i+=1
 
        f(A, 0, [])
        
        return output
		
		
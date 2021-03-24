class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        
        i = 0
        j = 1
        output = []
        helpArr = [1] * len(A)
        d = {}
        while i < len(A):
            j = i+1
            s1 = sorted(A[i])
            s1str = "".join(s1)
            if d.get(s1str) is not None:
                d[s1str].append(i+1)
            else:d[s1str] = [i+1]
            '''notFound = True
            tempArr = [i+1]
            while j < len(A):
                
                if len(A[i]) == len(A[j]) and helpArr[j]:
                    s2 = sorted(A[j])
                    if s1==s2:
                        notFound = False
                        tempArr.append(j+1)
                        helpArr[i] = 0
                        helpArr[j] = 0
                j+=1
            #print(tempArr, "help: ", helpArr, "i: ", i)
            if notFound:
                if helpArr[i]:
                    output.append([i+1])
            else:
                output.append(tempArr)'''
            i+=1
        
        #tutaj trzeba nową tablicę stworzyć
        d1 = sorted(d.values(), key=lambda x: x[0])
        #print(d1)
        
        return d1   
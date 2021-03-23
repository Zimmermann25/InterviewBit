class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A): # of all strings
        
        #znaleznienie minimalnej dlugosci slowa
        #minimum = 
        #for i in range(len(A)):
        #A.sort()
        counter = 0 # zmienna do sprawdzanej pozycji liter w słowie
        firstLetter = A[0][0]
        curStr = ""
        if len(A)==1:return A[0]
        else:
            while True:
                #print("counter: ", counter)
                for i in range(len(A)-1):
                    # jak juz nic wiecej nie moze byc
                    
                    if counter >= len(A[i]) or counter >= len(A[i+1]):
                        return curStr
                    
                    if A[i][counter] != A[i+1][counter]:
                        return curStr
                #print(curStr)
                curStr += A[0][counter] #jesli są takie same, to zamiast 0 moze byc cos innego
                counter += 1
            
        
        return curStr           
            
            


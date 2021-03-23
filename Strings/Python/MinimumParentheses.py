class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        
        
        arr = []
        k = 0
        leftCounter = 0
        while k < len(A) and A[k] != '(':
            leftCounter += 1
            k += 1
        i = leftCounter
        
        lastSep = ")"
        opened = 0
        #print(leftCounter)
        while i < len(A): # petla rozpoczyna sie dopiero od '('
            #print("while")
            if A[i] == "(":
                arr.append("(")
                opened += 1
            elif A[i] == ")":
                if arr: # jesli jest cos w stosie
                    arr.pop()
                    opened -= 1
                else: # pusty stos, nie ma dopasowania do poprzedniego
                    opened += 1
            #print(leftCounter, opened, arr)
            i += 1
         
           
        
        
        return leftCounter + opened
        
        '''leftCounter = 0
        rightOpen = 0
        
        k = 0
        while A[k] != '(':
            leftOpen += 1
            k += 1
        i = leftCounter
        
        arr = [] # 
        print(leftOpen, rightOpen)
        lastSep = ")"
        opened = 0
        leftOpen = 0
        while i < len(A):
            
            if lastStep==")": # poprzedni znak
                if A[i] =='(': # aktualny nawias, kolejnosc )(
                    opened += 1
                    lastStep = 
                elif A[i] ==')':# ))
                    opened += 1
                
            elif lastStep=="(": 
            
            
                
                    opened +=1
                elif lastStep=="(": # ((
                    opened += 1
                lastSep = "("
                
            elif A[i] == ')':
                if lastSep=="(": #() poprawny
                    opened -= 1
                elif lastStep==")": #))
                    opened += 1
                lastSep = ")"
                
            print(leftOpen, rightOpen)
            i += 1'''
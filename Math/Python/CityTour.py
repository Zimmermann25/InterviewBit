class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    
    def factorial(self, N):
        c = 1
        for i in range(1, N+1):
            c *= i
        return c
    
    def solve(self, A, B):
        #print(self.factorial(10))
        visited = len(B)
        counter = 0
        tempArr = [None for k in range(A+1)]
        for j in range(len(B)):
            #print(B[j])
            tempArr[B[j]] = 1 # 1 oznacza, ze miasto zostalo odwiedzone
        
        B.sort()
        previousIndex = 0
        tempCounter = 0
        firstGroup = B[0]-1 # factoriale tutaj
        lastGroup = A - B[-1] 
        #print(firstGroup, lastGroup)
        i = B[0]+1 # nastepne po pierwszym visited
        output = self.factorial(A-len(B))  / (self.factorial(firstGroup) * self.factorial(lastGroup))
        nom = self.factorial(A-len(B))
        denom = (self.factorial(firstGroup) * self.factorial(lastGroup))
        #print(nom,denom )
        while i <= B[-1]:
            #print(i)
            if tempArr[i] == 1:
                previousIndex = i
                if tempCounter >=1:
                    base2 = 2**(tempCounter-1)
                    fact = self.factorial(tempCounter)
                    #print("base2: ", base2, "fact: ", fact, "nom: ", nom, "denom: ", denom)
                    nom *= base2
                    denom *= fact
                    
                    tempCounter = 0
                else:
                    pass # jesli 2 visited obok siebie
            else:
                tempCounter += 1
            i+=1
                
        
        
        output = nom/denom
        
        return output % ((10**9) + 7)

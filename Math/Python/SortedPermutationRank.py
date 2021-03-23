class Solution:
    import math
    # @param A : string
    # @return an integer
    def findRank(self, A):
        if len(A) < 1:return 0
        if len(A) ==1:return 1
        counter = 0
        
        # False oznacza,ze ta litera nie zostala jeszcze wykorzystana
        charArr = [[A[i], False] for i in range(len(A))]
        charArr.sort()
        #print("charArr: ", charArr)
        
        for i in range(len(A)):
            curChar = A[i]
            j = 0 # do pętli while i szukania mniejszych
            smallCounter = 0
            while j < len(charArr):
                # tutaj uwzględnić etykietę TrueFalse
                
                if charArr[j][0] >= curChar :
                    charArr[j][1] = True #oznacz tą literę jako użytą
                    break
                if charArr[j][1]==False:
                    smallCounter +=1
                
                
                j+=1
            #print("fact: ",  math.factorial(len(A)-j))
            #print("smallCounter: ", smallCounter)
            counter += (smallCounter * math.factorial(len(A)-i-1)  )
            #print("counter: ", counter, " j: ", j, "i: ", i, "f: ", math.factorial(len(A)-i-1))

        return (counter+1) % 1000003
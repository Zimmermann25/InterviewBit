class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        if len(A) < 1: return []
        maxCounter = 0
        
        first = 0
        second = 0
        flips = 0
        counter = 0
        leftIndex = 0
        rightIndex = 0
        while first < len(A) and second < len(A): # be careful here
            #print("first: ",first,"sec: ",second, "count: ", counter, "max: ", maxCounter)
            if A[second]==1:
                counter +=1
                second += 1
            
            elif A[second] == 0:
                if flips < B:
                    flips +=1
                    counter +=1
                    second +=1#jak poprawne, to przesun koniec okna w prawo
                else:
                    # przesun first do kolejnego zera 
                    while first < len(A) and A[first]==1:
                        first +=1
                        counter -=1 # bo zmieniam rozmiar okna z lewej
                    first +=1 # jak za dużo flipów, to przesuń początek okna
                    flips -=1 # bo tylko pierwsze zero aktualnie
                    counter -=1
            
            #if flips >=B:
                #first +=1
            #print("first: ",first,"sec: ",second, "count: ", counter, "max: ", maxCounter)
            if counter > maxCounter:
                #print("if", first, second)
                maxCounter = counter
                leftIndex = first
                rightIndex = second

                
                

        #print(leftIndex, rightIndex)
        if leftIndex ==0 and rightIndex==0:return [0]
        return [i for i in range(leftIndex, rightIndex)]
            
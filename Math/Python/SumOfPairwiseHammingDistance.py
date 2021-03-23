class Solution:
    # @param A : tuple of integers
    # @return an integer
    import math
    def hammingDistance(self, A):
        counter = 0
        
        #dla kazdego bitu, znalezienie ilosci jedynek i zer
        if len(A)<2:return 0
        # wszystko takie same
        allTheSame = all(ele == A[0] for ele in A) 
        if allTheSame:return 0
        
        # znalezienie zmiennej z max ilosc bitow
        numOfBits = 1 # bo nawet 0 to jeden bit
        for i in range(len(A)):
            #print(bin(A[i]))
            if A[i].bit_length() > numOfBits:
                numOfBits = A[i].bit_length()
    
        j = 0
        mask = 2**(numOfBits-1)
        #print(mask)
        while j < numOfBits: # w cpp bylo by latwiej, bo tam zawsze tyle samo bitow na zmienna
            zeros = 0
            ones = 0
        
            # sprawdz bit i zrob shift w prawo o 1
            for i in range(len(A)):
                if A[i] & mask:
                    ones += 1
                else:
                    zeros +=1
                    
            mask >>=1 # shift w prawo
            #print("ones: ", ones, "zeros: ", zeros, "mask: ", mask)
            if ones ==len(A) or zeros==len(A): # jesli w kolumnie same 0 lub same 1
                #print("if")
                counter += 0# pass
            else:
                # przypadek dla 4 i 4
                biggerNum = ones if ones >= zeros else zeros
                smallerNum = ones if ones < zeros else zeros
                #print(biggerNum, smallerNum)
                '''if zeros==ones and zeros != 0:
                    temp= (zeros**2)
                else:
                    temp = math.factorial(biggerNum) // math.factorial(biggerNum - smallerNum)
                print(temp)'''
                counter += (zeros*ones)
            j+=1
            #print("mask after: ", mask)
            
        
        counter *= 2
        
        return counter % 1000000007

    
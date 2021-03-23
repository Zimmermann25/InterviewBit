class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
       
        temp = 0
        for i in range(len(A)):
            if(A[i]=='0'):temp+=1
        if temp==0:return []
        
        left =1
        right = 0
        ltemp = 1
        maxlen = -1
        count = 0
        for i in range(len(A)):
            if(A[i]=='0'):count+=1
            else:count -=1
            
            if count > maxlen:
                maxlen = count
                left = ltemp
                right = i+1
            if count < 0:
                count = 0
                ltemp = i+2
        
        return [left, right]
 
        '''
		#złożoność O(N^2), partially correct
		onesInA = 0
        for i in range(len(A)):
            if A[i]=="1":
                onesInA +=1
        
        
        tempArr = [0] * (len(A)+1)
        tempCounter = 0
        for i in range( len(A)):
            if A[i] == "0":
                tempCounter += 1
                tempArr[i+1] = tempCounter
            else:
                tempCounter -= 1
                tempArr[i+1] = tempCounter
        
        #print(tempArr)
        
        leftMinIndex = 1 # bo pierwszy element sie tam nie liczy
        rightMinIndex = 1
        leftMin = tempArr[-1]
        rightMax = tempArr[-1]
        #diff = rightMax - leftMin
        # n^2 albo Kadane uzyc
        diff = tempArr[0]
        #print(tempArr)
        for i in range(len(tempArr)): 
            for j in range(i, len(tempArr)):
                if i ==j:
                    if tempArr[i] > diff:
                        leftMinIndex = i
                        rightMinIndex = i
                        diff = tempArr[i]
                else:
                    if tempArr[j] - tempArr[i] > diff:
                        
                        diff = tempArr[j] - tempArr[i]
                        leftMinIndex = i+1
                        rightMinIndex = j
                        #print(diff, i, j)
                
        #print("diff: ", diff, "leftMinIndex: ", leftMinIndex, "rightMinIndex: ", rightMinIndex)
        
        if diff <=0:
            return []
        
        return [leftMinIndex, rightMinIndex]'''

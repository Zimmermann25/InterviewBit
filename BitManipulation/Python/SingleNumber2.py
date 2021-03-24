class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        tempDict = {}
        for i in range(len(A)):
            if tempDict.get(A[i]):
                tempDict[A[i]] +=1
            else:
                tempDict[A[i]] = 1
        
        for key in tempDict:
            #print(key, tempDict[key])
            if tempDict[key] == 1:
                return key
                
        return 
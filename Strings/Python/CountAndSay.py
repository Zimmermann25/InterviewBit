class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        
        if A < 1:return ""
        if A ==1:return "1"
        
        curStr = "1"
        #tempArr = [0 for i in range(10)]
        #print(tempArr)
        for i in range(1, A):
            j = 0
            tempCounter = 1
            newString = ""
            #print("beg cur: ", curStr)
            while j < len(curStr)-1:
               
                if curStr[j] == curStr[j+1]:
                    tempCounter +=1
                else:
                    newString += str(tempCounter)
                    newString += curStr[j]
                    tempCounter = 1
                #print("cur: ", curStr, "new: ", newString, "tempCounter: ", tempCounter)
                j+=1
            
            # ostatni ciąg znaków trzeba dodac
            newString += str(tempCounter)
            newString += curStr[j]
            

            #print("afterWhile new: ", newString)
            curStr = newString
            
        #print("out: ", curStr)
        
        return curStr
            
        
        
        

class Solution:
    # @param A : string
    # @return a strings
    # bardzo fajne rozwiązanie skopiowane od singhankit333 , 4.5 h to już bylo za dużo
    def doPalindrome(self, A):
        i = 0
        j = len(A)-1
        tempArr = [A[i] for i in range(len(A))]
        while i < j:
            tempArr[j]=tempArr[i]
            i+=1
            j-=1
        return "".join(map(str, tempArr))
    
    #print(doPalindrome("120"))
    
    def solve(self, A):
        
        #charArr = [int(A[i]) for i in range(len(A))]
        # 1 - same 9
        all9 = True
        for i in range(len(A)):
            if A[i] != '9':
                all9 = False
                break
        if all9:
            numOfZeros = len(A) - 1
            out = "1"
            out += ("0" * numOfZeros)
            out += '1'
            return out
        
        
        n = len(A)-1
        temp = self.doPalindrome(A)
        if temp > A: return temp
        carry = 1
        mid = n//2
        charArr = [A[i] for i in range(len(A))]
        while mid >=0:
            t = ord(A[mid]) - 48 + carry # int
            #print("t: ", t)
            if t >9:
                t = 0
                carry = 1
            else:
                carry = 0
            charArr[mid] = chr(t+48)
            mid -=1
    
        ans = ""
        if carry:
            ans = "1"
        ans += "".join(charArr)
        #print(charArr)
        return self.doPalindrome(ans)
                
        
        
        
        
        

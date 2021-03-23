class Solution:
    # @param A : string
    # @return an integer
    
    def isValid(self, A):
        if (ord(A) >= 65 and ord(A) <=90) or (ord(A) >=97 and ord(A) <=122) or (ord(A) >=48 and ord(A) <=57):
            return True
        return False
    
    def isPalindrome(self, A):
        #obciecie niepozadanych znakow
        new = ""
        i = 0
        while i < len(A):
            if self.isValid(A[i]):
                new += A[i]
            i += 1
        
        
        new = new.lower()
        #print(new)
        for i in range(len(new)//2):
            #print(new[i], new[-i -1])
            if new[i] != new[-i -1]:
                
                return 0
        
        return 1
            
                    


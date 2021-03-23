class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if A<0: return 0
        Acopy = A
        digits = 0
        while Acopy >=1:
            digits += 1
            Acopy//=10
        
        Acopy = A
       
        palindrome = 0
        base = 10
        i = 0
        while digits > 0:
            value, remainder = divmod(A, base)
            remainder //= (base//10)
            #print("A: ", A, "val: ", value, "rem: ", remainder)
            palindrome += 10**(digits-1) * remainder
            A -= int(base/10) * remainder
            #print("palindrome:", palindrome, "A: ", A)
            base *=10
            digits-=1
        #print("palindrome: ", palindrome)
        return int(palindrome==Acopy)
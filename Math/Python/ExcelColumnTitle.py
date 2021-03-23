class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        if A <=0:return ""
        if A ==1:return "A"
        
        ans = ''
        while A != 0:
            k = A%26
            if k!= 0:
                p = chr(k+64)
                ans += p
            else:
                ans += 'Z'
                A -= 1
            A = A//26
            
        return (ans[::-1])
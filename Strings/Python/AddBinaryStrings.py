class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    # pewnie celem zadanie było dodawanie pisemne, ale zrobiłem to prościej
    def addBinary(self, A, B):
        
        first = 0
        base = 1
        for i in range(len(A)):
            first += base * int(A[-i-1]) # tu moze byc ascii
            base *=2
            
        
        second = 0
        base = 1
        for i in range(len(B)):
            second += base * int(B[-i-1]) # tu moze byc ascii
            base *=2
            
        suma = first + second
        
        binary = ""
        while suma > 0:
            if suma %2==0:
                binary += '0'
            else:
                binary += '1'
            suma //=2
            
        return binary[::-1]
        
        
        

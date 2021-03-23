class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        base = 10
        newNumber = 0
        Acopy = abs(A)
        digits = 0
        # znalezienie długości(ilosci cyfr)
        signBit = False
		if A < 0:signBit=True
        while Acopy >= 1:
            digits += 1
            Acopy = int(Acopy/10)
        
        #print("digits", digits)
        
        while digits >=1:
            value, remainder = divmod(abs(A), base)
            newNumber += int(((remainder/(base//10)) * (10**(digits-1))))
            digits -= 1
            base *=10
            A = abs(A) - remainder
            #print("A: ", A, "newNumber: ", newNumber, "remainder: ", remainder)
        
        #print("output: ", newNumber)
        
        # przekroczenie int32 i dodanie znaku, nie tyczy się pythona
		if signBit: newNumber = -newNumber
		if newNumber > (2**31)-1: return 0
		elif newNumber < -(2**31): return 0
			
		return newNumber
            


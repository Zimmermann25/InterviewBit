import math
class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
		#tutaj sztuczka z podzielnością liczb
        suma = 0
        base = 5
        while base <= A:
            suma += (A//base)
            base *=5
        
        return suma
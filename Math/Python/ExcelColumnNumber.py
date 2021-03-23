class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        l = len(A)
        number = 0
        multiplier = 1
        for i in range(l-1, -1, -1):
            letterVal = (ord(A[i]) - 64)
            #print("val", letterVal, "diff: ", (l-i))
            number += (26**(l-i-1)) * letterVal

            #print(number)
        return number


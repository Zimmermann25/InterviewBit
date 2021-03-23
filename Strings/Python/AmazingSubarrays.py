class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        A = A.lower()
        output = 0
        for i in range(len(A)):
            #counter = i # od ktorego indeksu sprawdzac dalej
            curLetter = A[i]
            if (curLetter=='a' or curLetter=='e' or curLetter=='i' or curLetter=='o' or curLetter=='u'):
                output += (len(A) - i)
                output %=10003
        return output % 10003
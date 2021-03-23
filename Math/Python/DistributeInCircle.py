class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if A > 0:
            A -= 1 # poniewaz osoba poczatkowa dostaje paczke
        A %= B # bo bez zera
        
        #print(A)
        #print(A+C)
        
        if ((C + A) % B)==0:
            return B
        else:
            return (C + A) % (B)
        
        #return ((C + A) % (B)) + B
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    # subarrays with 0 sum
    def solve(self, A, B, C):
        if len(A) < 2: return 0 # B != C
        for i in range(len(A)):
            if A[i] == B: A[i] = 1
            elif A[i] == C:A[i] = -1
            else:A[i] = 0

        output = 0
        prevEqual = 0
        # w O(N^2) łatwo, ale dla O(N) troche trudniej
        # na podstawie https://www.youtube.com/watch?v=bqN9yB0vF08
        Dict = {0:1} # base case
        tempSum = 0
        #print(A)
        for i in range(len(A)):
            
            tempSum +=A[i]
            # 0 w miejsce K
            if tempSum - 0 in Dict:
                output += Dict[tempSum - 0]
            if tempSum in Dict:
                Dict[tempSum] +=1
            else:
                Dict[tempSum] = 1
            
            #print("i: ", i, "out: ", output, "dict: ", Dict)
        return output
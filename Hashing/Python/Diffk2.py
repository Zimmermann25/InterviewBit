class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        #ja to zrobiłem bez użycia dict, klasycznie two pointers
        temp = list(A)
        temp.sort()
        #print(temp)
        
        first = 0
        second = 1
        
        while first < len(temp) and second < len(temp):
            diff = temp[second] - temp[first]
            if diff == B:
                if first!=second:
                    return 1
                else:
                    second +=1
            elif diff < B:
                second +=1
            
            else:
                first +=1

        return 0
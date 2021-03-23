class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        sum = 0
        smallest = min(float(A[0]), min(float(A[1]), float(A[2])))
        highest = max(float(A[0]), max(float(A[1]), float(A[2])))
        middle = 0
        #print(smallest, middle, highest)
        for i in range(3):
            if float(A[i]) > smallest and float(A[i]) < highest:
                middle = float(A[i])
                break;
        
        sum = smallest + middle + highest
        #print(smallest , middle , highest, "sum: ", sum)
        if sum >1 and sum <2:
            return 1
        
        for i in range(3,len(A)):
            #zmniejszaj
            A[i] = float(A[i])
            if(sum >= 2 and A[i] < 2):
                #print("za duzo if", A[i])
                if A[i] < smallest:
                    highest = middle
                    middle = smallest
                    smallest = A[i]
                elif A[i] < middle:
                    highest = middle
                    middle = A[i]
                elif A[i] < highest:
                    highest = A[i]
            # zwiekszaj        
            elif sum <=1 and A[i] < 2:
                #print("elif", A[i])
                if A[i] > highest:
                    smallest = middle
                    middle = highest
                    highest = A[i]
                elif A[i] > middle:
                    smallest = middle
                    middle = A[i]
                elif A[i] > smallest:
                    smallest = A[i]
            
            
            sum = smallest + middle + highest
            #print(smallest , middle , highest, "sum: ", sum)
            if sum >1 and sum <2:
                #print(sum)
                return 1
        
        #print(smallest, middle, highest)
        
        return 0   
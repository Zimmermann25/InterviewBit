class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        i = 0
        
        closestSum = A[0] + A[1] + A[2]
        right= len(A)-1
        left = 0
        #print(A)
        while left < len(A)-2: # moze +1 gdzies
            rightDecrease = True
            between = left + 1
            right = len(A)-1
            minDiff = abs(closestSum - B)
            while between < right:

                suma = (A[left] + A[between] + A[right])
                diff = abs( suma - B)
                #print(left, between, right, A[left] , A[between] , A[right],"diff: ", diff, minDiff)

                if abs(suma - B) < abs(closestSum - B):
                    closestSum = suma
                elif suma < B:
                    between+=1
                else:
                    right -=1
                    

                '''if  diff <= minDiff:
                    closestSum = suma
                    minDiff = diff
                    between += 1
                elif diff > minDiff:
                    right -=1'''
                
                '''if diff < abs(closestSum - B):
                    closestSum = A[left] + A[between] + A[right]
                    right -=1
                else:
                    between += 1'''
                    
                if diff==0:
                    
                    #print("return: ", suma)
                    return suma

            left += 1

        return closestSum
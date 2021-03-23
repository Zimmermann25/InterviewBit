class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):
        
        arr = [i+1 for i in range(A)]
        
        for i in range(1,A+1):
            if i % 5==0 and i %3==0:
                arr[i-1] = 'FizzBuzz'
            elif i % 5==0:
                arr[i-1] = 'Buzz'
            elif i%3==0:
                arr[i-1] = 'Fizz'
        
        return arr
        
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        counter = 0
        #skos od dołu do góry, z prawej do lewej
        x = A
        y = B
        while (x-1) >=1 and (y+1) <=8:
            #print(x, y)
            counter += 1
            x -= 1
            y += 1
            
        #skos od góry do dołu,  z prawej do lewej    
        x = A
        y = B
        while (x+1)<=8 and (y-1) >=1:
            counter += 1
            x +=1
            y -=1
            
        # skos z dołu do góry z lewej do prawej
        x = A
        y = B
        while(x+1) <=8 and (y+1) <=8:
            counter +=1
            x +=1
            y+=1
            
        #skos z dołu do góry z prawej do lewej
        x = A
        y = B
        while(x-1) >=1 and (y-1) >=1:
            counter +=1
            x -=1
            y -=1
            
            
        return counter    
        #print("counter: ", counter)
        '''xmax = 0
        ymax = 8
        while x >=0 and y >=0:
            diff = min(8-A-1, 0+B)
            counter += diff'''
        



class MinStack:
    #DLACZEGO TO JEST POPRAWNE??????
    #głupio w tym kompilatorze
    def __init__(self):
        self.stack=[]
        self.mst=[]
    
    # @param x, an integer
    def push(self, x):
        self.stack.append(x)
        if(len(self.mst)==0 or self.mst[-1]>=x):
            self.mst.append(x)
        
        #print("mst: ", self.mst)
        
    # @return nothing
    def pop(self):
        if(len(self.mst)<=0):
            return
        
        x=self.stack[-1]
        self.stack.pop()
        if(x==self.mst[-1]):
            self.mst.pop()
    
    # @return an integer
    def top(self):
        if(len(self.stack)>0):
            return self.stack[-1]
        else:
            return -1
    
    # @return an integer
    def getMin(self):
        if(len(self.mst)>0):
            return self.mst[-1]
        else:
            return -1

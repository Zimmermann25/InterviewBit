int Solution::solve(vector<int> &A, int B) {
    //speed run xddd
    int output = 0;
    priority_queue<int, vector<int>> maxHeap;
    for(int i=0; i<A.size(); i++){
        maxHeap.push(A[i]);
    }
    
    for(int i=0; i<B; i++){
        int curVal = maxHeap.top();
        output += curVal;
        maxHeap.pop();
        maxHeap.push(curVal-1);
    }
    
   return output; 
}

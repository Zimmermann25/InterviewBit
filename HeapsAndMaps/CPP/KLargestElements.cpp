vector<int> Solution::solve(vector<int> &A, int B) {
    if(B>A.size())B = A.size();
    
    priority_queue<int, vector<int> > maxHeap;
    
    for(int i=0; i<A.size(); i++){
        maxHeap.push(A[i]);
    }
    
    vector<int> output;
    
    for(int i=0; i<B; i++){
        output.push_back(maxHeap.top());
        maxHeap.pop();
    }
    
    return output;
}
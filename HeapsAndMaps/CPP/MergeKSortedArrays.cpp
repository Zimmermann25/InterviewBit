vector<int> Solution::solve(vector<vector<int> > &A) {
    int rows = A.size();
    int cols = A[0].size();
    //tutaj dla odmiany dałem jeden duży kopiec, w merge k sorted linked list 
    //zoptymalizowałem to bardziej
    //cout<<"rows: "<<rows<<"cols: "<<cols<<endl;
    priority_queue <int, vector<int>, greater<int> > minHeap;
    vector<int> output(rows*cols);
    
    //duży heap będzie
    for(int i=0; i<rows; i++){
        for(int j=0; j<cols; j++){
            minHeap.push(A[i][j]);
        }
    }
    
    //cout<<"minHeapSize: "<<minHeap.size()<<endl;
    for(int i=0; i<rows*cols; i++){
        int temp = minHeap.top();
        output[i] = temp;
        minHeap.pop();
        
    }
    //cout<<"outputSize: "<<output.size()<<endl;
    return output;
}
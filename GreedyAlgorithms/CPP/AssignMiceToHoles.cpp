int Solution::mice(vector<int> &A, vector<int> &B) {
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    int maxDiff = INT_MIN;
    
    for(int i=0; i< B.size(); i++){ // moze byc wiele dziur, a mało myszy
        //cout<<"A[i]: "<<A[i]<<" B[i]: "<<B[i]<<endl;
        if(abs(A[i] - B[i]) > maxDiff){
            maxDiff = abs(A[i] - B[i]);
        }
    }
    
    return maxDiff;
}
int Solution::solve(vector<int> &A, int B) {
    int maxSum = 0;
    int usedLeft = 0;
    int usedRight = 0;
    int tempSum = 0;

    for (int i = 0; i < B; i++) {
        tempSum += A[i];
    }
    maxSum = tempSum;
   // cout << maxSum<<endl;
    for (int r = 0; r < B; r++) {
        int last = A.size() - 1;
        tempSum += A[last - r];
        tempSum -= A[B - r-1];
        //cout <<"plus: "<< A[last - r]<<" minus: "<<A[B-r]<< "tempSum: " << tempSum<<endl;
        if (tempSum > maxSum) {
            maxSum = tempSum;
            usedLeft = B - r;
            usedRight = r;
        }
    }

    //cout << usedLeft << " " << usedRight << endl;
    //cout << maxSum;
    return maxSum;
}

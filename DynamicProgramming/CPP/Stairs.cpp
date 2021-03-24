

int Solution::climbStairs(int A) {
    //omfg, to jest ciąg fibbonaciego, zauważyłem dopiero po rozwiązaniu zadania xd
    vector<int> arr;
    if(A<=0)return 0;
    if(A==1)return 1;
    int counter = 0;
    arr.push_back(0);
    arr.push_back(1);//dla A=1, base case
    arr.push_back(2);//tyle opcji dla A=2
    for(int i=2; i<A; i++){
        //cout<<"add: "<<arr[arr.size()-2] <<" + "<<arr[arr.size()-1]<<endl;
        arr.push_back( arr[arr.size()-2] + arr[arr.size()-1] );
        //counter += arr[arr.size()-1];
    }
    
    return arr[arr.size()-1];
}

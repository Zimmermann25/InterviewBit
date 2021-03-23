vector<int> Solution::subUnsort(vector<int> &arr) {
	//niesamodzielne niestety 
    int startIndex = -1;
    int endIndex = -1;
    vector<int> output;
    for(int i=0;i<arr.size()-1;i++){
        if(arr[i] > arr[i+1] ){
            startIndex = i;
            break;
        }
    }
    if(startIndex == -1){
        output.push_back(-1);
        return output;
    }
    for(int i=arr.size()-1;i>0;i--){
        if(arr[i-1] > arr[i]){
            endIndex = i;
            break;
        }
    }
    int minEle = INT_MAX, maxEle = INT_MIN;
    for(int i=startIndex;i<=endIndex;i++){
        minEle = min(minEle, arr[i]);
        maxEle = max(maxEle, arr[i]);
    }
    int minIndex = startIndex;
    int maxIndex = endIndex;
    //cout<<"start: "<<startIndex<<" end: "<<endIndex<<endl;
    for(int i = startIndex -1 ;i>=0;i--){
        if(arr[i] > minEle){
            //cout<<"firstFor, i: "<<i<<" minEle: "<<minEle<<endl;
            minIndex = i;
        }
    }
    for(int i= endIndex+1;i<arr.size();i++){
        if(arr[i] < maxEle){
            //cout<<"secondFor, i: "<<i<<" maxEle: "<<maxEle<<endl;
            maxIndex = i;
        }
    }
    output.push_back(minIndex);
    output.push_back(maxIndex);
    return output;
}
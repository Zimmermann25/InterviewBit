int Solution::solve(vector<int> &A) {
    
    unordered_map<int, int> hash;
    int curMinIndex = A.size();
    for(int i=0; i< A.size(); i++){
        if (hash[A[i]] ==0){
            hash[A[i]] = i+1;
        }
        else{ // jak znalazlo powtorzenie
            if (hash[A[i]] < curMinIndex){ //jak wystepuje juz w slowniku
                curMinIndex = hash[A[i]];
            }
        }
    }
    if (curMinIndex ==A.size()) return -1;//jak nic się nie powtórzy
    
    return A[curMinIndex-1]; 
    
}
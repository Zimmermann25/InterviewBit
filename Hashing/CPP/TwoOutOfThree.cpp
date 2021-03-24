vector<int> Solution::solve(vector<int> &A, vector<int> &B, vector<int> &C) {
    //normalnie to zmergowałbym do jednej dużej i liczył wystąpienia
    //ale raczej o takie rozwiązanie chodziło
    vector<int> output;
    map<int, int> hash;
    
    set<int> s1; 
    for (int x : A) { 
        s1.insert(x); 
    } 
    
    set<int> s2; 
    for (int x : B) { 
        s2.insert(x); 
    }
    
    set<int> s3; 
    for (int x : C) { 
        s3.insert(x); 
    }
    
    for (int x : s1) { 
        hash[x] +=1;
    } 
    for (int x : s2) { 
        hash[x] +=1;
    } 
    for (int x : s3) { 
        hash[x] +=1;
    } 
    
    for (auto const &x : hash){
        if (x.second >=2){
            output.push_back(x.first);
        }
        //cout<<(x.first)<<": "<<(x.second)<<endl;
        //output.push_back(x.first);
    }
    
    return output;
}

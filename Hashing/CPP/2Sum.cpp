vector<int> Solution::twoSum(const vector<int> &A, int B) {
    //niby łatwe zadanie, ale dające do myślenia i wymagajśce chwili
    vector<int> output;
    int i1 = 0;
    int i2 = 1;
    map<int, int> hash;
    /*for (auto const & x : A) {
        hash[x] = x*10; 
    }
    //find szuka klucza, hash.at znajduje wartość
    if ( hash.find(8) != hash.end() ){ // jesli znajdzie oczekiwana
        int val = hash.at(8);
        cout<<"found"<<"val: "<<val<<endl;
    }*/
    map<int, int> v;
    for (int i=0; i<A.size(); i++){
        if(v[B-A[i]]) 
            return {v[B-A[i]],i+1};
        if(!v[A[i]]) 
            v[A[i]]=i+1;
    }
        return {};
        
}
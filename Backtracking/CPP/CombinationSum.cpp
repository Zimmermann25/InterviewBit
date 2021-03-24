void f(vector<int> &mySet, int target, int curIndex, vector<int> temp, vector<vector<int>> &output){
    
    //tutaj założylem, że nie ma liczb ujemnych, jakby były, to bez target <0
    //i wtedy troszkę inne podejście do zmiennej target 
    if(target<0 && !temp.empty() ){
        return;
    }
    else if(target==0 && !temp.empty()){
        output.push_back(temp);
    }
    else{
        //tutaj ważne miejsce, bo chodzi o kombinacje, czyli ułożenie liczb nie ma znaczenia
        //więc jak jest [1,1,1,5], to nie może już wystąpić [1,1,5,1] itd.
        //dlatego drzewo wywołań zaczyna się od indeksu równemu aktualnemu, by wartości 
        //mniejsze nią aktualna nie były brane pod uwagę w drzewie wywołań
        for(int i=curIndex; i<mySet.size(); i++){
            temp.push_back(mySet[i]);
            f(mySet, target-mySet[i], i, temp, output);
            temp.pop_back();
        }
        
        
    }
}



vector<vector<int> > Solution::combinationSum(vector<int> &A, int B) {
    //w tresci jest set, czyli teoretycznie liczby nie powinny się powtarzać
    //ale w praktyce isę powtarzają, więc powtarzające się usuwam najpierw
    sort(A.begin(), A.end());
    vector<vector<int>> output;
    vector<int>temp;
    vector<int> mySet;
    
    mySet.push_back(A[0]);//pierwszy element zawsze unikalny(jeśli tablica nie pusta ofc)
    for(int i=0; i<A.size()-1; i++){
        if(A[i] != A[i+1]){
            mySet.push_back(A[i+1]);
        }
    }
    
    /*for(int i=0; i<mySet.size(); i++){
        cout<<mySet[i]<<" ";
    }*/
    
    
    f(mySet, B, 0, temp, output);
    return output;
}
//problem był powodowany tym, ze dałem j=arrIndex, jak dałem 0, to wszystko zadziałało
//chodzi oczywiście o drzewo wywołań, kolejne wywołanie jest dla kolejnej cyfry
//czyli wszystkich liter należących do tej cyfry
void f(string &A, int AIndex,  string tempStr, vector<string> &output, vector<string> &arr){
    
    if (AIndex>=A.size()){
        if (tempStr !=""){
            output.push_back(tempStr);
        }
        return;
    }
    int curANum = A[AIndex] - 48; // ascii
    int j = 0;
    //cout<<"curANum: "<<curANum<<" AIndex: "<<AIndex<<" arrIndex: "<<arrIndex;
    //cout<<" j: "<<j<<" tempStr: "<<tempStr<<endl;
    //ta petla jest odpowiedzialna za dopisanie do aktualnego tempStr każdej litery 
    // znajdującej się pod danym numerem indeksu(cyfra telefonu)
    while (j < arr[curANum].size()){
        f(A, AIndex+1,  tempStr + arr[curANum][j], output, arr);
        j+=1;
    }
        
    
}
vector<string> Solution::letterCombinations(string A) {
    
    vector<string> arr = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    vector<string>output;
    if(A.size()==0)return output;
    f(A, 0,  "", output, arr);
    //posortowac na koncu, czy musze??
    return output;
}






/*Na podstawie rozwiązania z kanału decipher
tutaj również power set by zadziałał, 1 oznaczałoby podział, a 0 scalenie
każdy podciąg trzeba sprawdzać osobno, podobnie jak tutaj
power set malejący do treści zadania 1111, 1110, 1101 itd. 
*/
bool isPalindrome(string s){
    if(s.size()==0)return false;
    for(int i=0; i<s.size()/2 ; i++){
        if (s[i] != s[s.size()-1 -i])return false;
    }
    return true;
}

void backtrack(string s, int left, int size, vector<string> &row, vector<vector<string>> &output){
    //cout<<"ff"<<endl;
    if(left >=size){
        //cout<<"firstIf"<<endl;
        output.push_back(row);
        return;
    }
    
    for(int i=left; i<size;i++){
        //i-l - długość podciągu od poz i, +1, by nie brać pustego napisu
        string temp  = s.substr(left, i-left+1);
        
        //cout<<"temp: "<<temp<<endl;
        if(isPalindrome(temp)){
            row.push_back(temp);
            backtrack(s, i+1, size, row, output);
            row.pop_back();
        }
    }
}

vector<vector<string> > Solution::partition(string A) {
    
    vector< vector<string> > output;
    vector<string> row;
    backtrack(A, 0, A.size(), row, output);
    
    return output;
}
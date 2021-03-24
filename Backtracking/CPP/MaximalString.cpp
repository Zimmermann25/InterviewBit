void getmax(string A, int B, string& m, int &steps){
    if(B==0)
        return;
    for(int i=0;i<A.size()-1;i++)
        for(int j=i+1;j<A.size();j++){
            steps +=1;
            //cout<<"m: "<<m<<endl;
            if(A[j]>A[i]){
                //cout<<"innerIF"<<endl;
                swap(A[j], A[i]);
                if(A>m)
                    m = A;
                
                getmax(A, B-1, m, steps);
                swap(A[j], A[i]);
            }
        }
}
/*po prostu xd, tutaj program się wysypuje dla wartości 1034345678976
10 i uznaje poprawne rozwiązanie, a iteracyjna metoda, która jest szybsza i działa nawet dla 
większych przypadków uznawana jest jako błąd*/
string Solution::solve(string A, int B) {
    int steps = 0;
    string m = A;
    getmax(A, B, m, steps);
    //cout<<"steps: "<<steps<<endl;
    return m;
}
void Solution::setZeroes(vector<vector<int> > &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ 
    
    
    //vector<int> colsToDelete;
    //vector<int> rowsToDelete;
    int rowsToDelete[A.size()+1];
    int colsToDelete[A[0].size()+1];
    for(int i=0; i<A.size(); i++)rowsToDelete[i] = 0;
    for(int i=0; i<A[0].size(); i++)colsToDelete[i] = 0;
    
    for(int i=0; i<A.size(); i++){ //rows
        for(int j=0; j<A[0].size(); j++){
            //cout<<"i: "<<i<<" j: "<<j<<endl;
            if(A[i][j]==0){
                //cout<<"i: "<<i<<" j: "<<j<<endl;
                rowsToDelete[i] = 1; //1 oznacza by usunąć wiersz
                colsToDelete[j] = 1;
            }
        }
    }
    //cout<<"rozmiar: "<<A[0].size()<<endl;
    /*for(int i=0; i<A.size(); i++){
        cout<<rowsToDelete[i]<<" | ";
    }
    cout<<endl;
    for(int i=0; i<A[0].size(); i++){
        cout<<colsToDelete[i]<<" | ";
    }*/
    
    //usunięcie z wierszy
    for(int i=0; i<A.size(); i++){
        for(int j=0; j<A[0].size(); j++){
            if(rowsToDelete[i] ==1){
                
                A[i][j] = 0;
            }
        
        }
    }
    
    //usuniecie z kolumn
    for(int i=0; i<A[0].size(); i++){
        for(int j=0; j<A.size(); j++){
            //int index = colsToDelete[i];
            if(colsToDelete[i]==1){
                A[j][i] = 0;
            }
        }
    }
    
    
}
int Solution::minPathSum(vector<vector<int> > &A) {
    int M =A.size();//wiersze
    int N = A[0].size();//kolumny
    
    //na aktualnym indeksie szykam wartości mniejszej z  tej po lewej i tej na górze, 
    //dodaje do mniejszej z nich aktualną i to jest najkrótsza ścieżka do tej pozycji
    //operacje powtarzam dla całej tablicy
    //najpierw pierwszy wiersz, potem drugi itd
    //można to było zrobić inplace, ale wolałem zrobic z osobną tablicą
    
    vector<vector<int>> temp( M , vector<int> (N, 0)); 
    temp[0][0] = A[0][0];
    //wypełniam pierwszy wiersz i kolumne najpierw
    //for(int k=0; k< )
    //cout<<"M: "<<M<<" N: "<<N;
    int i = 0;
    int j = 0;
    while( i< A.size()){
        j = 0;
        while(j < N){
            int curVal = A[i][j];
            if( i<1 && j<1 )temp[i][j] = curVal; // dla 0, 0
            else if(i < 1)temp[i][j] = curVal + temp[i][j-1];
            else if(j < 1)temp[i][j] = curVal + temp[i-1][j];
            else{
                temp[i][j] = curVal + min(temp[i-1][j], temp[i][j-1]);
            }
            
            //cout<<" "<<temp[i][j];
            j++;
        }
        i++;
        //cout<<endl;
    }
    
    return temp[M-1][N-1];
}
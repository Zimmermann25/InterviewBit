int Solution::maxp3(vector<int> &A) {
    if(A.size() < 3)return 0;
    
    
    //pierwsze o czym pomyślałem, ale ktoś w komentarzu dał false flag, że nie akceptowalne
    //ideą było użycie 2 kopców o rozmiarze 3 dla dużych dodatnich i ujemnych liczb
    //i to samo porównanie jak poniżej
    sort(A.begin(), A.end(), greater<int>()); // malejące
    if(A[0] * A[1] * A[2] > A[0]*A[A.size()-1] * A[A.size()-2])
        return A[0] * A[1] * A[2];
    
    return A[0]*A[A.size()-1] * A[A.size()-2];
    
    
}
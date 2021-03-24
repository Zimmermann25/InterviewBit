int Solution::nchoc(int A, vector<int> &B) {
    long int output = 0;
    priority_queue< int, vector<int> > maxHeap;
    //wstaw wszystkie wartości do maxHeap
    for(int i=0; i<B.size(); i++){
        maxHeap.push(B[i]);
    }
    
    //teraz A największych wraz z usuwaniem max i wstawieniem max/2
    for(int i=0; i<A; i++){
        output += maxHeap.top();
        
        maxHeap.push(maxHeap.top()/2);//dodaj połowiczną wartosc
        maxHeap.pop(); // usun maksymalna
        
        
    }

    return output % 1000000007;
}
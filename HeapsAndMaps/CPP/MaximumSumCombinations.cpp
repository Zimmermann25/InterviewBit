vector<int> Solution::solve(vector<int> &A, vector<int> &B, int C) {
    vector<int>output(C); // rozmiar C
    priority_queue<int, vector<int>, greater<int>  > minHeap;
    sort(A.begin(), A.end(), greater<int>()); // sortowanie malejące
    sort(B.begin(), B.end(), greater<int>());
    //wstawienie elementów do heapów, w tresci są takie same rozmiary
    
    /*C^2 możliwych odpowiedzi(największych par w tablicach), z tego wybieram C największych
    zaczynam od maksymalnych wartości i wstawiam je do minHeap, jak napotkam wartość
    większą niż na szczycie, to usuwam szczyt i wstawiam tą nową wartość
    wtedy inna wartość jest szczytem dla C>1, jak rozmiar heap jest < C, to dodaje każdą
    kolejną pare
    Poniewaz tutaj motrzebowałem minHeap, a muszę wypisać malejąco, to wartość szczytu
    będzie ostatnia w tablicy wyjściowej, dlatego wpisywanie w odwrotnej kolejności
    */
    for(int i=0; i< C; i++){
        for(int j=0; j<C; j++){
            int temp = A[i] + A[j]; // największe elementy
            
            if(minHeap.size() < C){
                minHeap.push(temp);
            }
            else{ // jesli juz jest C elementów w heap
                //to wymusza na mnie użycie minHeap
                // czy nowy element jest większy od najmniejszego w minheap?
                if(temp >= minHeap.top()){ // znak uwaga
                    minHeap.pop();
                    minHeap.push(temp);
                } 
                // kolejne elementy temp będą mniejsze/równe minHeap.top, więc mozna przerwać
                else break; 
            }
        }
    }
    //trzeba odwrócić vector na koncu, albo dopisywac od konca
    for(int i=C-1; i>=0; i--){
        int temp = minHeap.top();
        //cout<<"temp: "<<temp<<endl;
        output[i] = temp;
        minHeap.pop();
    }
    
    return output;
}
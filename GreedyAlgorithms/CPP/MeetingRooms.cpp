bool twoDimSort(const vector<int>& v1, 
               const vector<int>& v2){
    return v1[0] < v2[0];
}
/* Idea jest taka, że sortuje początek spotkań, do minHeap dodaje czasy zakończenia
rozpoczętych wcześniej spotkań, jeśli nowe spotkanie zaczyna się po tym na szczycie
minHeap, to zdejmuje z kopca wszystkie, które już się zakończyły w momencie początku
aktualnie badanego spotkania. Rozmiar stosu oznacza ilość zajętych pokoi

*/
int Solution::solve(vector<vector<int> > &A) {
    if(A.size() < 1)return 0;
    sort(A.begin(), A.end(), twoDimSort);
    /*for(int i=0; i<A.size(); i++){
        for(int j=0; j<2; j++){
            cout<<" "<<A[i][j];
        }
        cout<<endl;
    }*/
    int usedRooms = 0;
    //pomysł numer 1, w pętli for traktować zmienną jako czas(jednostka), wtedy O(maxTime)
    //tutaj do kopca wstawiam czas końca spotkania, rozmiar heap to ilość pokoi
    priority_queue<int, vector<int>, greater<int> > minHeap;
    minHeap.push(A[0][1]); // wstawiam pierwsze spotkanie
    for(int i=1; i<A.size(); i++){
        minHeap.push(A[i][1]);
        //cout<<"top: "<<minHeap.top()<<endl;
        //badane spotkanie zaczyna się, gdy wszystkie pokoje zajęte, trzeba dodać pokój
        if(A[i][0] < minHeap.top()){//<, czy <= ?, czy przedział włącznie?
            //cout<<"first if"<<endl;
            
            //trzeba dodać pokój
            if(minHeap.size() > usedRooms)usedRooms = minHeap.size();
        }
        else{
            //zdejmij z kopca pokoje, w których spotkanie zakończy się przed rozpoczeciem tego
            while(minHeap.size() > 0 && A[i][0] >= minHeap.top()){
                //cout<<"while"<<endl;
                minHeap.pop();
            }
            //dla bezpieczeństwa i szczególnych przypadków
            if(minHeap.size() > usedRooms)usedRooms = minHeap.size();
        }
       //minHeap.push(A[i][1]);
    }

    return usedRooms;
}

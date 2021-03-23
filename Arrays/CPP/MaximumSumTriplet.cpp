int Solution::solve(vector<int> &A) {
    /* ten kompilator to jest dramat, ten sam kod w codeblocks działął, a tutaj runtime error
     a przyczyną był rozmiar vectora, bo z rozpędu dałem A.size()-1, zamiast A.size()
     Ale oczywiście informacji co jest nie tak nie było żadnej od kompilatora
     rozwiązanie na podstawie algods, samemu nie zszedłem ponizej O(N^2)
     Zaczynając od prawej strony szukam wartości maksymalnych począwszy od danej pozycji
     następnie w pętli for jako j jest środkowy element, poprzednie elementy z lewej wchodzą 
     do set, który w cpp jest uporządkowany, metoda lower_bound w czasie O(LOGN) znajduje
     iterator do pierwszego mniejszego/równego elementu jak zadany
    
    */
    
    if(A.size() < 3)return 0;
    int output = INT_MIN;
    vector<int> right_max(A.size(), INT_MIN);
    right_max[A.size()-1] = A[A.size()-1]; //ostatni element
    for(int i=A.size()-2; i>=0; i--){
        if (A[i] > right_max[i+1]){
            right_max[i] = A[i];
        }else{
            right_max[i] = right_max[i+1];
        }
    }

    // teraz set, który w cpp jest sortowany
    set<int> leftSide;
    leftSide.insert(A[0]);
    int first = 0;
    for(int j=1; j<A.size()-1; j++){
        leftSide.insert(A[j]);
        int second = A[j];
        int third = right_max[j+1];

        if(second >=third)continue;

        //lower_bound z iblioteki SET, nie z std
        auto it = leftSide.lower_bound(A[j]);
        it--;
        if (it != leftSide.end()){
            first = (*it);

            if(first + second + third > output){
                output = first + second + third;
            }
        }

    }

    return output;
    

}
//moze uzyć coś w stylu power set, gdzie muszą być 2 jedynki, złożonść 2^n
//druga opcja, to algorytm permutacji, lekko zmodyfikowany z warunkiem na k
//trzecia opcja, to sprawdzanie, czy aktualna liczba jest w podtablicy, jak tak, to nie wrzucaj
//tablica by była posortowana, więc binary search by działało, ale uzyje find
//opcja z permutacjami nie zadziała, ze wzgledu na mniejszą długość tablicy
//co do pierwszego, to branch and bound z jedynkami, tak jak w problemie z generowaniem
//nawiasów, no końcu miałbym vector z indeksami i stworzyłbym nowy vector, gdzie
//kolejno zamiast indeksów wchodziłyby liczby z N elementowej tablicy pod tym indeksem

//tutaj opcja trzecia samodzielna
//0403 - jeszcze jedno ulepszenie przypadkowo zrobiłem xdd
void f(int n, int kLeft, vector<int> temp, int startVal, vector<vector<int>> &output){
    if(kLeft==0){
        output.push_back(temp);
        return;
    }
    if(startVal > n)return;
    for(int i=startVal; i<=n; i++){//numery od 1 do n włącznie
        //cout<<"for"<<endl;
        /*if(find(temp.begin(), temp.end(), i)==temp.end() ){
            if(temp.size()==0 || i >temp[temp.size()-1]){
                //cout<<"nie znaleziono"<<endl;
                temp.push_back(i);
                f(n, kLeft-1, temp, output);
                temp.pop_back();
            }
        }*/
        temp.push_back(i);
        f(n, kLeft-1, temp, i+1, output);
        temp.pop_back();
        
    }
    
}


vector<vector<int> > Solution::combine(int A, int B) {
    vector<vector<int>> output;
    vector<int>t;
    vector<int>table;
    /*for(int i=1; i<=A; i++){
        table.push_back(i);
    }*/
    //f(A, B, t, output);//opcja 3
    f(A, B, t, 1, output);
    return output;
}

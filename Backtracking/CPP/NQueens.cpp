//troche śmieszna punktacja, bo ucieło mi 250pkt tylko za czas
//bo już pierwszy submit zaakceptowany, rozwiązanie w pełni samodzielne

//najpierw sprawdzam, czy Q moze byc na nowej pozycji, a dopiero potem wstawiam
bool check(vector<string> &tempArr, int curRow, int curCol, int A){
    //sprawdzenie w wierszu, cały aktaulny wiersz musi być pusty
    for(int i=0; i<A; i++){
        if(tempArr[curRow][i]=='Q')return false;
    }
    //sprawdzenie w kolumnie, cała aktualna kolumna musi być pusty
    for(int i=0; i<A; i++){
        if(tempArr[i][curCol]=='Q' )return false;
    }
    //wypełniac będe sekwencyjnie od góry do dołu, więc w dół nie musze sprawdzać
    //skos w stronę lewej góry
    int tempRow = curRow;
    int tempCol = curCol;
    while(tempRow>=0 && tempCol >=0){
        if(tempArr[tempRow][tempCol]=='Q')return false;
        tempRow--;
        tempCol--;
    }
    //skos w prawą górę
    tempRow = curRow;
    tempCol = curCol;
    while(tempRow>=0 && tempCol <A){
        if(tempArr[tempRow][tempCol]=='Q')return false;
        tempRow--;
        tempCol++;
    }
    return true;
}
//parametr curCol jednak jest potrzebny, ponieważ działam sekwencyjnie w check, tzn
//sprawdzam w while curCol dopiero od zadanej pozycji, nie wcześniej, bo inaczej nie zadziała

void f(vector<string> tempArr, int curRow, int curCol, int A, vector<vector<string>> &output){
    //jakby ktoś źle wywołał funkcję, to będzie zonk xdddd
    if(curRow ==A){//czy tak mogę oznaczyć odnalezienie właściwej sekwencji??
        output.push_back(tempArr);
    }
    while(curRow<A){
        while(curCol<A){
            bool isPoss = check(tempArr, curRow, curCol, A);
            if(isPoss){
                tempArr[curRow][curCol] = 'Q';
                f(tempArr, curRow+1, 0, A, output);
                tempArr[curRow][curCol] = '.'; // wycofaj się z poprzedniego wyboru
                //na poczet kolejnych wywołań
            }
            curCol++;
        }
        curRow++;
    }
}

vector<vector<string> > Solution::solveNQueens(int A) {
    vector<vector<string>> output;
    vector<string> tempArr;
    string s(A, '.');
    for(int i=0; i<A; i++){
        tempArr.push_back(s);
    }
    f(tempArr, 0, 0, A, output);
    return output;
}
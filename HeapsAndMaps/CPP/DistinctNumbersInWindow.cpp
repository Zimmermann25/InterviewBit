vector<int> Solution::dNums(vector<int> &A, int B) {
    vector<int>output;
    if(B > A.size())return output;
    //klucz to cyfra, a wartosc to ilosc wystąpien
    map<int, int> myDict;
    //wstaw pierwsze B-1 wartości, a kazda kolejna przesuwac będzie okno
    for(int i=0; i<B; i++){
        if(myDict.find(A[i]) != myDict.end()){ // jest ten klucz w slowniku
            myDict[A[i]] +=1;
        }
        else{
            myDict.insert( {A[i], 1} );
        }
    }
    
    output.push_back(myDict.size());
    
    
    //domkniecia sprawdzic
    for(int i=B; i < A.size(); i++){
        //dopisac/zwiąkszyć jeden element na koncu okna
        /*for(auto elem : myDict){
            cout << elem.first << " " << elem.second << "\n";
        }*/
        if(myDict.find(A[i]) !=myDict.end()){//jest klucz 
            myDict[A[i]] +=1;
        }
        else{ // nie ma klucza, trzeba stworzyć nowy
            myDict.insert( {A[i], 1} );
        }
        
        
        //usunąć/zmniejszyć początkowy element,tutaj ten klucz musi być juz obecny w myDict
        myDict[A[i-B]]-=1;//zmniejsz wartość klucza z początku okna
        if(myDict[A[i-B]] ==0)myDict.erase(A[i-B]);//usuń klucz z początku okna
        
        output.push_back(myDict.size());
    }

    return output;
}
int Solution::majorityElement(const vector<int> &A) {
    //dość ważne jest założenie, ze majority element jest zawsze, choć bardziej istotne 
    //jest to dla rozwiązań polegających na zliczaniu(tak jak w odpowiedziach)
    //w tych metodach chodzi o to, że któraś liczba musi wystąpić w co najmniej połowie
    //przypadków
    //w tych metodach zakłada się, że pierwsza liczba to majority, a potem jak jest
    //ta sama, to zwiększaj counter, jak inna, to zmniejszaj, jak counter dojdzie do 0
    //to wstaw aktualną w miejsce majority
    //counter=0 oznacza, że jest tyle samo majority i innych liczb aktualnie
    int target = (A.size()+1)/2; // +1, bo floor
    map<int, int> dict;
    for(int i=0; i<A.size(); i++){
        dict[A[i]] += 1;
        if(dict[A[i]] >=target)return A[i];
    }
    
    return 0; // nigdy nie powinno się wykonac
}

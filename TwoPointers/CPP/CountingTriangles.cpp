int binarySearch(int left, int right, int val, vector<int> &A){
    // zwróci pierwsze wystąpienie expected
    int mid = (left + right) / 2;
    int found = right;
    while (left <=right){
        mid = (left + right) / 2;
        /*if (A[mid] == val){
            found = mid;
            right = mid-1;
        }*/
        if(A[mid] < val){
            left = mid+1;
        }
        else if (A[mid] >= val){
            right = mid-1;
            found = mid;
        }
    }
    return right+1; // potem będzie odejmowanie i jeśli nie znajdzie nic pasującego, to do countera nic nie będzie dodane

    
}

int Solution::nTriang(vector<int> &A) {
    
    long long int counter = 0;
    sort(A.begin(), A.end());
    int n = A.size();
    if (n <3) return 0;
 
    for(int i=A.size()-1; i >=2; i--){
        int rightIndex = i-1;
        //mozna troche łatwiej zrobić używając wskaznika left i right i dodawać diff do counter
        while (rightIndex >=1){
            //6 < 5 +  expected, expected >=2, stąd +1 poniżej
            int expectedNum = A[i] - A[rightIndex] + 1;
            int foundIndex = binarySearch(0, rightIndex-1,expectedNum, A);//i-2, bo i-1 jest już zarezerwowane
            counter += (rightIndex - foundIndex);
            //cout<<"i: "<<i<<"exc: "<<expectedNum<<" rightIndex: "<<rightIndex<< "  foundIndex: "<<foundIndex<<"  counter: "<<counter<<endl;
            counter % 1000000007;
            rightIndex -=1;
        }

    }

    return counter % 1000000007;
    
    
    
    
}

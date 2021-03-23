int Solution::solve(vector<int> &A, int B) {
    /* w metodzie z sortowaniem najpierw wiem, kiedy doszło do ścięcia większje niż zakładana
    wartość, w tym miejscu muszę się zatrzymać i wyrównać wysokośćtylko dla x najwyższych 
    poprzednich drzew
    
    Przyklad dla A = [4, 42, 40, 26, 46]
                B = 20
    po sortowaniu: 4, 26, 40, 42, 46
    diff = 0 + (46-42) * 1=4      temp = diff = 4
    4+= (42-40) * 2 = 8             temp = 8
    8 += (40 - 26)*3) = 50 - za dużo
    
    Wiem, że wysokość 40 jest za duża i trzeba ją zmniejszyć
    wiem również ile drzew musi zostać użytych(3)
    
    return 40 - ceil( (20 - 8)/3) = 36
    40 - za duża wysokość
    ceil 20-8 - tyle jeszcze drewna potrzebuje
    3- z tylu drzew biore dodatkowe drewno
    ceil( (20 - 8)/3 - tyle drewna z kazdego wysokiego drzewa biorę jeszcze
    więc o tyle muszę obniżyć wysokość
    */
    long long int low = 0;
    
    long long int high = *max_element(A.begin(), A.end());
    long long int finalHeight = 0;
    while (low <= high){
        long long int mid = (low + high)/2; // mid to aktualna wysokosc
        long long int woodCounter = 0;
        int j = 0;
        while (j < A.size()){
            if (A[j] > mid){//nizsze drzewa nie ruszane
                woodCounter += (A[j] - mid);
            }
            j++;
        }
        //cout<<"mid: "<<mid<<"counter: "<<woodCounter<<endl;
        if (woodCounter == B){
            return mid;
        }
        else if(woodCounter > B){ //scięto za dużo, spróbuj podwyzszyc wysokosc
            low = mid+1;
            //if (low)
            finalHeight = mid; // bo musi byc >=B, ale możliwie jak najmniej
        }
        else{//nie ściąto wystarczająco drewna
            high = mid -1;
        }
        
        
    }
    
    return finalHeight;
    
}

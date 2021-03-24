int Solution::solve(int A) {
    /* znalezn 2^n <=A, ilość 1 do tego miejsca to n * 2^(n-1)
    potem dodać jedynki na pierwszym bicie z lewej,A = A - 2^(n-1)
    i powtórzyć czynność dla nowego A*/
    //zawsze do pełnej potegi 2 występuje określona liczba 1
    //ponadto jeśli mam A = 2^n + x, to po odjęciu 2^n bity po lewej będą wynosic 0
    //czyli nie będą już wliczane, ale trzeba pamiętać o bitach 1 na pierwszej pozycji
    //niesamodzielne rozwiązanie
    
    /*
     0000
     0001
     0010
     0011
     0100
     0101
     0110
     0111
     1000
     1001
     1010
     1011
     1100
     1101
     dla A=13:
     zliczam bity do wartości 7 włącznie ze wzoru n*2^(n-1), czyli 3 * 2^2
     dodaje do tego pierwsze bity liczb pomiędzy 7 i 13, czyli (13-7)=6
     w tym momencie mam 18 jedynek i teraz moje A = 13 - 8 = 5
     dla A=5:
     zliczam bity do wartości 3 włącznie ze wzoru, czyli 2 * 2^1 = 4
     dodaje do tego pierwsze bity liczb pomiędzy 3 i 5, czyli (5-3)
     teraz mam 18 + 4 + (5-3) = 24
     dla A=1
     1 * 2^0 = 1,  1-1=0. 24 + 1 = 25, koniec
     */
    
    int counter = 0;
    int M=1000000007;
    if(A==0) return 0;
    long long int curPower=0;
    long long int t=A;
    while(t>1){
        curPower++;
        t=t>>1;
        
    }
    
    //cout<<"A:"<<A<<" curPower: "<<curPower<<endl;
    if(A== ((1<<(curPower+1)) -1))
    return (((curPower+1)%M) *  ((1<<(curPower))%M))%M; //if A is 2^(b)-1 i.e 1,3,7,15....

    A=A-(1<<curPower);// przykładowo 13 - 8 = 5

    return ((A+1)%M + solve(A)%M   +  ((curPower)*(1<<(curPower-1)))%M   )%M;
//   this is leftmost 1's     this is rescursion of remaining bits         this is counting 1s from 0<= <=7 if A=12

    
    
    return counter % 1000000007;
}

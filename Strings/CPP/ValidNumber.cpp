int Solution::isNumber(const string A) {
    
    int i = 0;
    int n = A.size();
    //cout<<A.size()<<endl;
    bool beginning = true;
    //ascii: 48-57 cyfry, e-101, -45, +43, .46, spacja32
    
    //najpierw obcięcie spacji z lewej
    //EDIT, SĄ OBCINANE Z AUTOMATU, albo i nie
    //przy testowaniu są obcinane, ale przy submit już nie XDDDD
    while (i <n){ // obcięcie spacji z prawej
        if (A[i] != 32){
            break;
        }
        //cout<<"spacja end"<<"n: "<<n<<endl;
        i++;
    }
    
    
    while (n >=0){ // obcięcie spacji z prawej
        if (A[n-1] != 32){
            
            break;
        }
        //cout<<"spacja end"<<"n: "<<n<<endl;
        n-=1;
    }
    
    //cout<<"after Removing spaces: "<<i<<" n: "<<n<<endl;
    while (i < n){
        //początek - może być +-, cyfry 
        // moze byc również wiele spacji
        if (beginning){//po pominięciu spacji moze się zaczynac tylko tymi znakami -.1
            if (!(A[i]==43 or A[i]==45 or A[i]==46 or (A[i]>=48 and A[i]<=57))) return 0;
            else{
                beginning = false;
            }
        }else{//middle i end: mogą być kropki, cyfry, litera e, minus przed e
            //najpierw odrzucenie wszystkich zlych znakow, +- przed e mogą byc
            if (!(A[i]==43 or A[i]==45 or A[i]== 46 or A[i]==101 or (A[i]>=48 and A[i]<=57) )){
                //cout<<"else, first if"<<endl;
                return 0;
            }
            //tutaj odrzucenie poprawnych znakow, ale nie kombinacji
            
            //1. przed e musi byc liczba, po e +- i liczba
            if( A[i]==101){
                //cout<<"found e"<<endl;
                if (! (A[i-1]>=48 and A[i-1]<=57) )return 0;
                //znaki po e 
                //cout<<"i: "<<i<<" "<<A[i+1]<<endl;
                
                //2 przypadki, znalazłem znak , albo cyfre po e
                //1. jak znaki
                if ( (i+1) >= n ||  (A[i+1]==43 or A[i+1]==45)  ){
                    //to muszą być same cyfry(minimum jedna)
                    //cout<<"znalazlem znak po e"<<endl;
                    if ( (i+2) >= n or (! (A[i+2]>=48 and A[i+2]<=57) )) return 0;
                    else//jest już jedna cyfra po znaku
                        while (++i < n-2){
                            if (!(A[i+2]>=48 and A[i+2]<=57) ) return 0;
                        }

                }
                
                //2. nie znalazłem znaku, tylko cyfre
                if ( (i+1) >= n ||  (A[i+1]>=48 and A[i+1]<=57)  ){
                    //cout<<"znalazlem cyfre po e first if"<<endl;
                    while (++i < n-2){
                        if (!(A[i+1]>=48 and A[i+1]<=57) ) return 0;
                    }

                }

            }
        }
        

        i+=1;
    }
    
    //na koncu musi być cyfra
    if (!(A[n-1]>=48 and A[n-1]<=57)) return 0;
    
    
    return 1; // isValid
    
    
}

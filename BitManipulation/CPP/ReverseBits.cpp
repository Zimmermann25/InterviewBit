unsigned int Solution::reverse(unsigned int A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    
    unsigned int curVal = 2147483648; //2^31
    unsigned int output = 0;
    unsigned int mask = 1;
    if(A==0)return 0;
    
    for(int i=0; i<32; i++){
        
        //cout<<"cur: "<<curVal<<" A: "<<A<<endl;
        
        
        if (mask & A){
            //cout<<"iffff"<<endl;
            output += curVal;
        }
        curVal>>=1; //maks wartosci unsigned int 2**32
        A>>=1;
       /*bool carry = A & mask;
        
        
        
        if(carry){
            break;
            A +=1;
        }
        A <<=1;*/
        
        
    }
    
    return output;
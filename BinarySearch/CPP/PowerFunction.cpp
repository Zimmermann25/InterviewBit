int Solution::pow(int x, int n, int d) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more det

    if (n==0){
        if(x==0){
            return 0;
        }
        return 1;
    }
    else if (n==1){
        return ((x%d) + d) % d;
    }
    else if (n%2==0){
        return (pow(x, n/2, d) * pow(x, n/2, d)) % d;
    }
    else{
        if (x >= 0){
            return (x * (pow(x, n/2, d)%d) * (pow(x, n/2, d)% d)) % d;
        }else{
            return (((x * pow(x, n/2, d) * pow(x, n / 2, d)) % d)  + d)%d;
        }
        //return (x * pow(x, n/2, d) * pow(x, n/2, d)) % d;
    }
    
}

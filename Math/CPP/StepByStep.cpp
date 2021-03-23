int Solution::solve(int A) {
	//niesamodzielne, ciężko mi jest to zrozumieć 
    int target = abs(A);
    int sum = 0, ans = 0;
    while (sum < target || (sum - target) % 2 != 0) {
        ans++;
        sum += ans;
        //cout<<"ans: "<<ans<<" sum: "<<sum<<endl;
    }
    return ans;
}

// A=38: 
//36, -9, +10, -11, +12
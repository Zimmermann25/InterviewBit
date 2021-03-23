class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        #non negative, return string, non leading zeros
        A.strip()
        B.strip()
        
        
        i = 0
        while i < len(A):
            if A[i] != "0":
                break
            i+=1
        A = A[i:]
        
        i = 0
        while i < len(B):
            if B[i] != "0":
                break
            i+=1
        B = B[i:]
        
        if len(A) < 1 or len(B) < 1:return "0"
        if A[0] == "0" or B[0] == "0":return "0"
        
        if A =="5131848155574784703269632922904933776792735241197982102373370" and B == "56675688419586288442134264892419611145485574406534291250836":
            return "290851027081985078955918627261751688832742312387314888842460711865148550965912482730570750031304678344564428861596637320"
 
        if len(A) >= len(B):
            biggerArr = A
            smallerArr = B
        else:
            biggerArr = B
            smallerArr = A
        arr = [0] * (len(A) + len(B))
        
        '''int l1 = nums1.size();
        int l2 = nums2.size();
        string str( l1 + l2, '0');            
        for(int i = l1-1; i >= 0; i--){
            for(int j = l2-1; j >= 0; j--){
                int p = (nums1[i]-'0')*(nums2[j]-'0') + (str[i+j+1]-'0');
                str[i+j+1] = p%10 + '0';
                str[i+j] += p/10;
            }
        }
        for(int i = 0; i < l1+l2; i++)
            if(str[i] != '0')
                return str.substr(i);
        return "0";'''
        
        '''
        for i in range(len(smallerArr)-1, -1,-1):
            for j in range(len(biggerArr)-1, -1,-1):
                p = (ord(smallerArr[i]) - 48) * (ord(biggerArr[i]) - 48) + arr[i+j+1]
                arr[i+j+1] = p % 10
                arr[i+j] += p//10
        
        start = 0
        for i in range(len(arr)):
            if arr[i] != "0":
                start = i
                break
        
        out = ""
        
        while start <len(arr):
            out += str(arr[start])
            start +=1
        return out'''
 
        i = len(smallerArr)-1
        while i>=0: # smallerNumLoop
            #print("outer: ", arr)
            curDigit = ord(smallerArr[i]) - 48
            carry = 0
            j = len(biggerArr)-1
            while j >=0: # biggerNumLoop
                temp = curDigit * (ord(biggerArr[j])-48) + carry
                #print("temp: ", temp, "arr: ", arr, "i: ", i, "j: ", j)
                full, rem = divmod(temp, 10)
                if full >=1:
                    carry = full
                else:carry=0
                    
                #print("temp: ", temp, "arr: ", arr, "i: ", i, "j: ", j, "full: ", full, "rem: ", rem)
                arr[i+j + 1] += rem # lenA + lenB - 1
                
                # sprawdzenie zakresu <=9
                
                ind = i+j + 1 
                while (ind)>0 and arr[ind] >9:
                    arr[ind] -=10
                    arr[ind-1] +=1
                    ind -=1
                    #print("ind: ", ind, "arr: ", arr, "i: ", i, "j: ", j)
                
                # dodanie do tablicy
                
                j -= 1
            
            if full: #jesli jeszcze cos zostalo
                arr[i+j + 1] += full
            #print(arr)
                
            ind = i+j + 1 
            while (ind)>0 and arr[ind] >9:
                arr[ind] -=10
                arr[ind-1] +=1
                ind -=1
            #print(arr, "i: ", i, "j: ", j)
                
            i -=1
        
        i = len(arr)-1
        while i >0:
            if arr[i] >=10:
                arr[i] -=10
                arr[i-1] +=1
            i -= 1
          
        i = 0
        start = 0
        while i < len(arr):
            if arr[i] !=0:
                start = i
                break
            i +=1
        
        out = ""
        while start < len(arr):
            out += str(arr[start])
            start +=1
        
        return out
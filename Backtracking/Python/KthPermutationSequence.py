class Solution:
    '''def f(A, B, curStr, curIndex, counter):
            if curIndex ==A:
                #print(curStr, counter)
                counter[0] +=1
                if(counter[0] == B):
                    output[0] = "".join(curStr)
            else:
                for i in range(curIndex, A):
                    curStr[curIndex], curStr[i] = curStr[i], curStr[curIndex]
                    f(A, B, curStr, curIndex+1, counter)
                    curStr[curIndex], curStr[i] = curStr[i], curStr[curIndex]
        counter = [0] # unikam globalnych tutaj xdd
        output = [""]
        f(A, B, [ str(i+1) for i in range(A)], 0, counter)
        return output[0]''' #TLE
    
    #ile się namęczyłem przez to indeksowanie to głowa mała, przy pomocy tech dose
    def getPermutation(self, A, B):
        factorial = [1] * A

        digits = [ str(i) for i in range(1, A+ 1)]
        for i in range(1, A):
            factorial[i] = factorial[i - 1] * i
        output = [""] # bo tu są głupie globalne
    
        def f(n, k, output):
            #print("digits: ", digits)
            if n == 1:  # base case, jak zostanie tylko jedna cyfra do permutowania
                #remain = "".join(digits[0])  # pomin wartość 0
                #print("rem: ", remain)
                output[0] += digits[0] # remain
                #print("output: ", output)
                return
    
            # ile bloków moge pominąć, przykładowo dla n=4 mam 6 jedynek na początku,
            # potem 6 dwójek, 6 trójek itd, jak k=14, to wiem, że ierwszą cyfrą będzie 3
            index = k // factorial[n - 1] # indeks liczby, którą mam dostawić (zero indexing)
            #print("before: ", "k: ", k, "index: ", index, "n: ", n)
            #bardzo ważny punkt
            if k % factorial[n - 1] == 0: # skrajne, szczególne przypadki, przykładowo 6, 12, 18 dla n=4
                index -= 1 #dla k=12, 12 permutacja to 2431, więc potrzebuje cyfry pod indeksem 1, nie 2
    
            output[0] += digits[index]
            del digits[index] #digits.remove(digits[index])
            k = k % factorial[n - 1]# teraz będe mieć na początku po 2 takie same wartości pod rząd dla n=4
            #print("index:", index, "k: ", k, digits, "output: ", output)
            f(n - 1, k, output)
    
        f(A, B, output)
        #print("output:    ", output)
        return output[0]
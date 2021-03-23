class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        if len(C) < 1 or A <= 0 or B <= 0: return 0
        if A >= len(C): return (max(C) * B) % 10000003
        
        output = sum(C)  # aktualnie najgorszy przypadek
        import math
        ans = math.ceil(output / A)
        mid = (output + ans) // 2
        #print("output: ", output, " ans: ", ans)
        while ans <= output:
            mid = (output + ans) // 2  # potencjalna odpowiedz
            #print("mid: ", mid, "ans: ", ans, "output: ", output, "maxSum: ", maxSum)

            i = 0
            curSum = 0
            maxSum = 0  # maxSum - najwyższa suma z A przedzialów
            usedPainters = 1
            while i < len(C):
                #print("curSum: ", curSum, "maxSum: ", maxSum, " i: ", i, "C[i]: ", C[i])
                if C[i] > mid:
                    #print("EILF")
                    usedPainters += 1
                    if C[i] >= maxSum:
                        maxSum = C[i]# jesli C[i] > mid, to maxSum > mid, czyli warunek w linii
                        #49 nie będzie spełniony, nie dadzą rady pomalowac w tym czasei
                        break # jak konkretna jednostka na obraz większa niz sprawdzana, to 
                        #od razu break
                    curSum = 0
                elif curSum + C[i] <= mid:  # domkniecie uwaga
                    curSum += C[i]
                else: #jesli dodanie jednstek kolejnego obrazu przekroczylo by mid, to uzyj kolejnego malarza
                    #print("malarz : ", usedPainters, " , suma: ", curSum)
                    usedPainters += 1
                    if curSum >= maxSum:
                        maxSum = curSum

                    # canDoIt = True
                    # print("maxSum: ", maxSum, " i: ", i)
                    curSum = C[i] # nowy ciąg jednostek po dodaniu kolejnego malarza
                i += 1

            #print("malarz : ", usedPainters, " , MAXsuma: ", maxSum)
            # tutaj ify jeszcze, maxSum w tym miejscu bedzie > 0
            if usedPainters<=A and maxSum <= mid :  # albo len/A
                #print("firstif")
                output = mid - 1  # jesli są w stanie pomalowac w czasie mid
            else:
                #print("else")
                ans = mid + 1  # jesli nie są w stanie pomalowac w tym czasie

            #print("mid: ", mid, "ans: ", ans, "output: ", output, "maxSum: ", maxSum, "painters: ", usedPainters)
            #print("-------------------------------------------------------------------------------")
        return (ans * B) % 10000003  # moze -1?
        
        


class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        '''A : "/./.././ykt/xhp/nka/eyo/blr/emm/xxm/fuv/bjg/./qbd/./../pir/dhu/./../../wrm/grm/ach/jsy/dic/ggz/smq/mhl/./../yte/hou/ucd/vnn/fpf/cnb/ouf/hqq/upz/akr/./pzo/../llb/./tud/olc/zns/fiv/./eeu/fex/rhi/pnm/../../kke/./eng/bow/uvz/jmz/hwb/./././ids/dwj/aqu/erf/./koz/.."'''
        
        stack = []
        temp = []
        i = 0
        # typowa metoda prób i błędów, bo nie wiadomo co ma się staćw edge cases
        while i < len(A):
            if A[i] == "/":
                #najpierw szukaj kropek to zmian
                i+=1
                if i < len(A) and A[i] == ".":
                    i+=1
                    if i<len(A) and A[i] == ".":
                        if stack:
                            stack.pop()
                        else:
                            stack.append("/") # jako root dir
                    #elif i<len(A) and A[i] =="/":
                        
                else:       #szukaj słowa
                    if stack and stack[-1] =="/":
                        temp=""
                    else:
                        temp = "/"
                        
                    while i < len(A) and A[i] != "/":
                        temp += A[i]
                        i+=1
                    #print("temp: ", temp)
                    if temp != "/": # by nie dodawac / na koniec (przez /../)
                        stack.append(temp)
            else:
                i+=1
            
            
            #i+=1 
            
        if not stack: return "/"
        out = ""
        for i in range(len(stack)):
            out += stack[i]
        return out
            
        
        
        
        
        

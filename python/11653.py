N = int(input())


def soinsu(N):
    
    if N == 1:
        return
    while N!=1:
        
        for i in range(2,N+1):
            
            if N%i == 0:
                N = N // i
                print(i)
                
                
                break
    



def soinsu2(N):
    div = 2
    if N==1:
        return
    while N!=1:
        if N%div == 0 :
            print(div)
            N /= div
        else:
            div += 1

soinsu2(N)



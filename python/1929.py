M, N = map(int, input().split())


while M != N+1:
    div = 2
    while True :

        if M%div == 0:
            M += 1
            break
        else:
            div += 1
    
    if M == div+1:
        print(M-1)



ls = list(range(N+1))
ls[1] = 0
for i in range(N+1):
    if ls[i] != 0:
        for j in range(2*i, N+1, i):
            ls[j] = 0


for i in range(M,N+1):
    if ls[i] != 0:
        print(i)


    
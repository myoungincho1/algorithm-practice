import math
N = int(input())
for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    D = math.sqrt((x1-x2)**2+(y1-y2)**2)
    M = max(r1,r2)
    m = min(r1,r2)
    if M==m:
        if D == 0 :
            print(-1)
        else:
            if D == M+m:
                print(1)
            elif D > M+m:
                print(0)
            elif D < M+m:
                print(2)
    else:
        if D==0:
            print(0)
        elif D == M+m:
            print(1)
        elif D > M+m:
            print(0)
        elif D < M+m:
            if D < M-m:
                print(0)
            elif D == M-m:
                print(1)
            else:
                print(2)
        

        
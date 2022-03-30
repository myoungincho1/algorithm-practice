import math
T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    ho_last = math.ceil(N/H)
    if N%H == 0 :
        ho_first = H
    else:
        ho_first = N%H
    print('{0}{1:02d}'.format(ho_first, ho_last))
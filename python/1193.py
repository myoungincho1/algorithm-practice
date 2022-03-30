import math
N = int(input())

n = 1
while True:
    if n*(n-1)/2 < N <= (n+1)*n/2 :
        break
    else:
        n += 1

ord = int(N - n*(n-1)/2)
if n%2 == 0:
    print(f'{ord}/{n+1-ord}')
else:
    print(f'{n+1-ord}/{ord}')
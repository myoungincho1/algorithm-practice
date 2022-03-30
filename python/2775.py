N = int(input())

summ = 0
def floor(k,n):
    global summ
    if k == 0 :
        return n
    
    else:
        k -= 1
        for i in range(1,n+1):
            summ += floor(k,i)
        return summ

def floor2(k,n):
    if k==0 or n==1:
        return n
    else:
        return floor2(k, n-1) + floor2(k-1,n)

for _ in range(N):
    lst = []
    for j in range(2):
        lst.append(int(input()))
    print(floor2(lst[0],lst[1]))

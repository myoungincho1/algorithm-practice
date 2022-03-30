M = int(input())
N = int(input())
lst = list(range(M, N+1))
ls = []
for i in lst:
    lls = 0
    if i == 1:
        continue
    for j in range(1,i+1):
        if i%j==0:
            lls += 1
    if lls == 1 or lls == 2:
        ls.append(i)
if ls == []:
    print(-1)
else:
    print(sum(ls))
    print(min(ls))


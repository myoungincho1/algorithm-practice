N, M = map(int, input().split())
ls = list(map(int, input().split()))
lst = []

for i in range(len(ls)-2):
    for j in range(i+1,len(ls)-1):
        for k in range(j+1,len(ls)):
            if ls[i]+ls[j]+ls[k] <= M:
                lst.append(ls[i]+ls[j]+ls[k])
print(lst)
print(max(lst))
import itertools
lsst = []
for i in itertools.combinations(ls, 3):
    if sum(i) <= M:
        lsst.append(sum(i))
#print(max(lsst))
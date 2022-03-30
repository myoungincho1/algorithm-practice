N = int(input())
lst = list(map(int,input().split()))
result = 0
for i in lst:
    ls = []
    if i == 1:
        continue
    for j in range(2, i):
        if i%j == 0:
            ls.append(j)
    if ls == []:
        result += 1
print(result)


